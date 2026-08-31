import os, sys, json, datetime, winreg
from pathlib import PureWindowsPath, PurePosixPath

LOG_FILE = "C:\\Program Files (x86)\\ossec-agent\\active-response\\active-responses.log"
ADD_COMMAND, DELETE_COMMAND, CONTINUE_COMMAND, ABORT_COMMAND = 0, 1, 2, 3
OS_SUCCESS, OS_INVALID = 0, -1
USBSTOR_KEY = r"SYSTEM\CurrentControlSet\Services\USBSTOR"

class message:
    alert = ""
    command = 0

def write_debug_file(ar_name, msg):
    with open(LOG_FILE, mode="a") as log_file:
        name = str(PurePosixPath(PureWindowsPath(ar_name[ar_name.find("active-response"):])))
        log_file.write(f"{datetime.datetime.now():%Y/%m/%d %H:%M:%S} {name}: {msg}\n")

def set_usb_start_value(value):
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, USBSTOR_KEY, 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, "Start", 0, winreg.REG_DWORD, value)
    winreg.CloseKey(key)

def setup_and_check_message(argv):
    input_str = sys.stdin.readline()
    write_debug_file(argv[0], input_str)
    try:
        data = json.loads(input_str)
    except ValueError:
        message.command = OS_INVALID
        return message
    message.alert = data
    command = data.get("command")
    message.command = ADD_COMMAND if command == "add" else DELETE_COMMAND if command == "delete" else OS_INVALID
    return message

def send_keys_and_check_message(argv, keys):
    keys_msg = json.dumps({"version": 1, "origin": {"name": argv[0], "module": "active-response"},
                            "command": "check_keys", "parameters": {"keys": keys}})
    write_debug_file(argv[0], keys_msg)
    print(keys_msg); sys.stdout.flush()
    input_str = sys.stdin.readline()
    write_debug_file(argv[0], input_str)
    try:
        action = json.loads(input_str).get("command")
    except ValueError:
        return OS_INVALID
    return CONTINUE_COMMAND if action == "continue" else ABORT_COMMAND if action == "abort" else OS_INVALID

def main(argv):
    write_debug_file(argv[0], "Started")
    msg = setup_and_check_message(argv)
    if msg.command < 0:
        sys.exit(OS_INVALID)

    if msg.command == ADD_COMMAND:
        alert = msg.alert["parameters"]["alert"]
        keys = [alert["rule"]["id"]]
        action = send_keys_and_check_message(argv, keys)
        if action != CONTINUE_COMMAND:
            write_debug_file(argv[0], "Aborted" if action == ABORT_COMMAND else "Invalid command")
            sys.exit(OS_SUCCESS if action == ABORT_COMMAND else OS_INVALID)
        try:
            set_usb_start_value(4)  # 4 = Disabled
            write_debug_file(argv[0], f"USB storage disabled (rule {keys})")
        except Exception as e:
            write_debug_file(argv[0], f"Failed to disable USB storage: {e}")

    elif msg.command == DELETE_COMMAND:
        try:
            set_usb_start_value(3)  # 3 = Manual (default/enabled)
            write_debug_file(argv[0], "USB storage re-enabled")
        except Exception as e:
            write_debug_file(argv[0], f"Failed to re-enable USB storage: {e}")

    write_debug_file(argv[0], "Ended")
    sys.exit(OS_SUCCESS)

if __name__ == "__main__":
    main(sys.argv)
