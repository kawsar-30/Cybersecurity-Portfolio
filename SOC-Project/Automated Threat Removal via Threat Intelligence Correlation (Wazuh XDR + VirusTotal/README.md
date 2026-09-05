# 🛡️ Automated Threat Removal via Threat Intelligence Correlation (Wazuh XDR + VirusTotal)

## 📌 Project Overview
This project implements a production-grade Security Orchestration, Automation, and Response (SOAR) pipeline using **Wazuh XDR** and **VirusTotal API**. It detects unauthorized file drops via real-time File Integrity Monitoring (FIM), cross-references the file hash against global threat intelligence, and executes an automated endpoint threat containment script to neutralize malicious assets without manual SOC intervention.

## 🏗️ Architecture & Workflow
1. **Detection (FIM):** Wazuh Agent continuously monitors the target directory (`d:\active-response test`) on the Windows endpoint for unauthorized file drops (**Rule 554**).
2. **Threat Intelligence Correlation:** The Wazuh Manager intercepts the event, extracts the file hash, and queries the VirusTotal API. A positive malicious match across multiple security engines triggers a critical alert (**Rule 87105**).
3. **Automated Active Response:** Upon receiving the critical alert, the Wazuh Active Response engine triggers a custom mitigation script (`remove-threat.exe`) on the endpoint (**Rule 100092**).
4. **Containment & Remediation:** The endpoint confirms the permanent deletion of the threat (**Rule 553**), completely neutralizing the payload within seconds.

## 📂 Repository Structure
* **`configs/`**: Contains Wazuh configurations for FIM monitoring (`fim_monitoring_config.xml`) and VirusTotal/Active Response integration (`active_response_config_&-virus_total_integration_config.xml`).
* **`python-script/`**: The custom Active Response Python/executable script (`remove-threat.py`) deployed on the endpoint.
* **`docs/`**: Project documentation, compiled PDF reports, and visual evidence screenshots (`virustotal-alert-rule-87105.png`, `active-response-remediation-rule-100092.png`).

## ⚙️ Setup Instructions
1. Append the VirusTotal integration and Active Response blocks to `/var/ossec/etc/ossec.conf` on the Wazuh Manager.
2. Configure the real-time FIM directory block in the endpoint's `ossec.conf` (`C:\Program Files (x86)\ossec-agent\ossec.conf`).
3. Deploy the threat removal script to the Windows Agent at: `C:\Program Files (x86)\ossec-agent\active-response\bin\`.
4. Restart the Wazuh Manager service (`sudo systemctl restart wazuh-manager`) to apply changes.

---
*Developed by MD. Kawsar Hossain | Cyber Security Analyst & Penetration Tester*
