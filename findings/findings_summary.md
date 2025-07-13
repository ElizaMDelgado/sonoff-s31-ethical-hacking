# 🔐 Security Findings Summary: Sonoff S31

This section documents confirmed and potential vulnerabilities discovered during ethical testing of the Sonoff S31 smart plug.

| ID   | Title                        | Severity | Status     | Link |
|------|------------------------------|----------|------------|------|
| F01  | Unauthenticated Local API    | High     | Confirmed  | [View](unauthenticated_local_api.md) |
| F02  | MQTT Configuration Injection | Medium   | Confirmed  | [View](mqtt_config_injection.md) |
| F03  | OTA URL Misuse               | High     | Confirmed  | [View](ota_misuse.md) |
| F04  | UART Shell Access            | High     | Confirmed  | [View](uart_shell_access.md) |
| F05  | No Firmware Signature Check  | High     | Observed   | _Pending write-up_ |

---

## 🚦 Status Key
- **Confirmed** – Reproduced and tested
- **Observed** – Identified via static or dynamic analysis
- **Pending** – Still being tested or documented

## 🔍 Notes
All findings were discovered and validated on a lab-controlled Sonoff S31 device. No third-party systems were impacted.
