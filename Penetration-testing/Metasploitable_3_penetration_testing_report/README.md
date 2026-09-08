# Metasploitable 3 - Vulnerability Assessment and Penetration Testing (VAPT)

This repository contains the comprehensive Penetration Testing report for the **Metasploitable 3** vulnerable virtual machine. The assessment was conducted following standard industry methodologies to identify, exploit, and document critical security flaws in a simulated enterprise network.

**Prepared by:** MD. Kawsar Hossain (Cyber Security Analyst & Penetration Tester)
**Project Branding:** ShieldCore Security

## 🎯 Project Overview
- **Target Environment:** Metasploitable 3 
- **Target Network:** Internal LAN (`192.168.0.105`)
- **Methodology:** Penetration Testing Execution Standard (PTES) & OWASP Guidelines

## 🛑 Key Findings & Exploitations
During the assessment, multiple critical vulnerabilities were successfully exploited to gain administrative and root-level access:
* **Apache Continuum:** Remote Code Execution (RCE)
* **Drupalgeddon:** SQL Injection & Remote Code Execution
* **ProFTPD:** Arbitrary File Write
* **UnrealIRCd:** Backdoor Command Execution

## 🛠️ Tools Utilized
* Nmap (Network Discovery & Service Enumeration)
* Metasploit Framework (Exploitation)
* SearchSploit (Vulnerability Research)
* OpenSSH & Git (Documentation & Deployment)

## 📄 Documentation
The complete, detailed VAPT report—including the executive summary, technical execution steps, screenshots, and remediation recommendations—is available in this repository. 

## ⚠️ Disclaimer
All penetration testing activities documented in this repository were conducted in a strictly controlled, isolated local lab environment. This project is intended solely for educational purposes and portfolio demonstration.
