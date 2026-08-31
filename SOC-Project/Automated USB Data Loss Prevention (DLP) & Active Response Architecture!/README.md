# 🛡️ Automated USB Data Loss Prevention (DLP) & Active Response

## 📌 Project Overview
This project implements an automated Threat Containment and Data Loss Prevention (DLP) pipeline using **Wazuh (XDR)** and **Python**. It detects unauthorized USB mass storage devices via Windows Registry telemetry and instantly triggers an Active Response script to disable the USB port, preventing potential data exfiltration or malware injection.

## 🏗️ Architecture & Workflow
1. **Detection:** Wazuh Agent monitors the Windows Event Logs and Registry (`USBSTOR`).
2. **Alerting:** Wazuh Manager triggers **Rule 100016** upon detecting a new USB mass storage connection.
3. **Active Response:** The Manager automatically executes a Python-based Active Response script (`usb_prevent_ar_script.py`) on the target endpoint.
4. **Containment:** The script alters the registry to disable the USB storage service, effectively blocking access.

## 📂 Repository Structure
* **`configs/`**: Contains the Wazuh XML configurations (`usb_dlp_rule.xml`, `active_response_config.xml`).
* **`python_script_script/`**: The Active Response Python script deployed on the endpoint.
* **`docs/`**: Project documentation, PDF reports, and visual proof (screenshots) of the triggered alerts and logs.

## ⚙️ Setup Instructions
1. Copy the contents of `configs/usb_dlp_rule.xml` to `/var/ossec/etc/rules/local_rules.xml` on the Wazuh Manager.
2. Append the Active Response configuration from `configs/active_response_config.xml` to the Manager's `ossec.conf`.
3. Deploy `usb_prevent_ar_script.py` to the Windows Agent at: `C:\Program Files (x86)\ossec-agent\active-response\bin\`.
4. Restart the Wazuh Manager service to apply changes.

---
*Developed by MD. Kawsar Hossain | Cyber Security Analyst & Penetration Tester*
