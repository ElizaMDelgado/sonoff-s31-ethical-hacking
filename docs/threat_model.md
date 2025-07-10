# 🛡️ Threat Model: Sonoff S31 Smart Plug

## 1. Overview
The Sonoff S31 is a Wi-Fi–enabled smart plug used to remotely control and monitor electrical devices. It connects to a local network and cloud-based services, making it an attractive target for attackers.

## 2. Assets at Risk
- Electrical device control (e.g., turning appliances on/off)
- Network integrity and privacy
- User credentials (if stored locally)
- Firmware and OTA update process

## 3. Potential Threat Actors
- **Remote attackers**: Attempting to exploit open ports or APIs over the internet.
- **Local attackers**: Within Wi-Fi range or on the same LAN.
- **Physical attackers**: With physical access to the device (e.g., through UART).

## 4. Possible Attack Vectors
| Vector | Description | Impact |
|--------|-------------|--------|
| Unauthenticated local API access | Commands accepted without authentication | Device hijack |
| Weak or hardcoded credentials | Static credentials stored in firmware | Unauthorized access |
| Insecure OTA update | Lack of signature verification | Malicious firmware injection |
| UART debug interface | Exposed serial access points | Full system control |

## 5. Impact Severity
- **High**: Unauthorized device control, persistent firmware tampering
- **Medium**: Privacy leakage, network enumeration
- **Low**: LED control, user annoyance

## 6. Assumptions
- The device is connected to a standard home router with no additional firewall rules.
- Attackers may gain physical access in a lab or testing environment.


