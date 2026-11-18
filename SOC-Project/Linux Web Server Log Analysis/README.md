# Linux Web Server Log Analysis & Incident Response Lab

## 📌 Project Overview
This repository documents a simulated real-world Incident Response (IR) and Threat Hunting investigation targeting an internal Linux web server. The project covers the complete attacker lifecycle—from reconnaissance and web application exploitation to root privilege escalation, local persistence, and subsequent SOC containment, eradication, and forensic log analysis.

---

## 🏗️ Lab Architecture & Network Topology
* **Attacker Machine:** Kali Linux (`192.168.0.106`)
* **Target Server:** Ubuntu Linux / Apache running DVWA (`192.168.0.109`)

![Topology Diagram](./diagrams/network-topology.png)

---

## 🔍 Investigation & Forensic Evidence

### Phase 1: Reconnaissance & Initial Access
* **Activity:** Automated vulnerability scanning followed by insecure file upload exploitation.
* **Evidence:** Apache access logs (`access.log.1`) showing Nmap script probes and consecutive `POST` requests to `/dvwa/vulnerabilities/upload/`.
> ![Recon & Upload Logs](./screenshots/02-initial-access-upload.png)

### Phase 2: Execution & Shell Spawning
* **Activity:** Triggering the malicious web shell (`shell.php`) via HTTP GET and spawning a reverse shell upgraded to an interactive PTY bash shell.
* **Evidence:** Process telemetry (`ps aux`) confirming `www-data` executing the Python pseudo-terminal spawn.
> ![Process Telemetry](./screenshots/04-process-telemetry.png)

### Phase 3: Privilege Escalation & Persistence
* **Activity:** Elevating execution context to root via `sudo` and establishing a shadow administrative backdoor account (`sysdebug`).
* **Evidence:** Authentication logs (`auth.log`) capturing the `useradd` execution and `/etc/passwd` verification.
> ![Auth Log Evidence](./screenshots/05-privilege-escalation-auth.png)

### Phase 4: Network Socket Audit & Containment
* **Activity:** Identifying active socket connections and executing emergency containment procedures.
* **Evidence:** Socket state utility output (`ss -tnp`) verifying active TCP connections prior to process termination.
> ![Socket State](./screenshots/07-network-sockets.png)

---

## 🛡️ MITRE ATT&CK Framework Mapping

| Tactics | Techniques | ID | Observed Activity / Evidence |
| :--- | :--- | :--- | :--- |
| **Reconnaissance** | Active Scanning | `T1595` | Nmap script engine probing (`access.log`) |
| **Initial Access** | Exploit Public-Facing Application | `T1190` | DVWA file upload POST requests |
| **Execution** | Command and Scripting Interpreter | `T1059.004` | Python PTY shell spawning (`ps aux`) |
| **Privilege Escalation** | Sudo and Sudo Caching | `T1548.003` | Root escalation via sudo (`auth.log`) |
| **Persistence** | Create Account: Local Account | `T1136.001` | Backdoor user `sysdebug` creation |

---

## 🛑 Remediation & Hardening Actions
1. **Socket Isolation:** Forcefully terminated malicious connection threads using signal-9 (`kill -9`).
2. **Artifact Eradication:** Purged uploaded scripts from the web root (`/var/www/html/dvwa/hackable/uploads/*`).
3. **Account Revocation:** Deleted the persistence account and home directory via `userdel -r sysdebug`.
4. **Server Hardening:** Disabled script execution capabilities inside web upload directories.
