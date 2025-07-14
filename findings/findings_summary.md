# 🔐 Security Findings Summary: Sonoff S31

This section documents confirmed and potential vulnerabilities discovered during ethical testing of the Sonoff S31 smart plug.

| ID   | Title                           | Severity | Status     |
|------|----------------------------------|----------|------------|
| F01  | Unauthenticated Local API Access | High     | Confirmed  |
| F02  | MQTT Configuration Injection     | Medium   | Confirmed  |
| F03  | OTA URL Misuse                   | High     | Confirmed  |
| F04  | UART Shell Access                | High     | Confirmed  |
| F05  | Missing Firmware Signature Check | High     | Observed   |

---

## 🚦 Status Key
- **Confirmed** – Reproduced and tested
- **Observed** – Identified via static or dynamic analysis
- **Pending** – Still being tested or documented

## 🔍 Notes
All findings were discovered and validated on a lab-controlled Sonoff S31 device. No third-party systems were impacted.
