# 🛡️ Automated SSH Brute-Force Mitigation & Jira SOAR Integration

## 📌 Project Overview
This project implements an automated Threat Containment and Incident Ticketing pipeline using **Wazuh (XDR)** and **Jira (SOAR)**. It detects high-velocity SSH brute-force attacks via Ubuntu authentication logs and instantly triggers a `firewall-drop` Active Response to block the attacker's IP. Simultaneously, it automatically generates a tracking ticket in Jira, preventing potential unauthorized access and streamlining SOC documentation.

## 🏗️ Architecture & Workflow
1. **Detection:** Wazuh Agent monitors the Ubuntu endpoint's authentication logs (`/var/log/auth.log`) for `sshd` failures.
2. **Alerting:** Wazuh Manager triggers custom **Rule 5720 (Level 12)** upon detecting multiple SSH login failures (MITRE ATT&CK T1110).
3. **Active Response:** The Manager automatically executes the `firewall-drop` Active Response script on the target Linux endpoint.
4. **Containment & Ticketing:** The script uses `iptables` to drop all connections from the attacker's IP. Simultaneously, a Python REST API webhook generates an incident ticket (`KAN-98`) in Atlassian Jira Cloud.

## 📂 Repository Structure
* **`configs/`**: Contains the Wazuh XML configurations (`ssh_bruteforce_rule.xml`, `active_response_ossec.xml`, `integration_ossec.xml`).
* **`python_scripts/`**: The custom integration script (`custom-jira-webhook.py`) used to parse alerts and forward them to the Jira API.
* **`docs/`**: Project documentation, architecture diagrams, and visual proof (screenshots) of the terminal logs, triggered alerts, and Jira tickets.

## ⚙️ Setup Instructions
1. Copy the contents of `configs/ssh_bruteforce_rule.xml` to `/var/ossec/etc/rules/local_rules.xml` on the Wazuh Manager.
2. Append the Active Response and Jira integration configurations from the `configs/` folder to the Manager's `/var/ossec/etc/ossec.conf`.
3. Deploy the webhook script (`custom-jira-webhook.py`) to the Wazuh Manager at: `/var/ossec/integrations/` and ensure it has the correct execute permissions (`chmod 750`).
4. Restart the Wazuh Manager service to apply all changes.

---
*Developed by MD. Kawsar Hossain | Cyber Security Analyst & Penetration Tester*
