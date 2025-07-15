#  Testing Methodology: Sonoff S31 Ethical Hacking

## 1. Objective
The primary goal of this project is to ethically analyze the security posture of the Sonoff S31 smart plug, identify potential vulnerabilities, and explore ways to improve its resilience against unauthorized access and misuse.

---

## 2. Testing Scope
- **Device Tested**: Sonoff S31 (flashed with both stock firmware and Tasmota version 15.0.1)
- **Environment**: Isolated local Wi-Fi network, private lab setting
- **Access Level**: Full physical access, including UART and firmware dump capabilities
- **Ethical Boundaries**: No testing against production environments or third-party networks

---

## 3. Testing Approaches

### 🔍 3.1 Blackbox Testing
Testing the device without prior knowledge of its internal code or configuration:
- Used `nmap` and `tcpdump` to identify open ports and protocols
- Issued HTTP requests using `curl`, `Postman`, and `Burp Suite` to discover undocumented API endpoints
- Tested device behavior to unauthenticated and malformed inputs

### 🔬 3.2 Whitebox Testing
Performed with firmware-level access and system visibility:
- Extracted firmware via UART and OTA backup
- Analyzed configuration settings, HTTP response structures, and internal logs from the Tasmota UI
- Verified if security settings (e.g., login enforcement) were implemented or enforced in local endpoints

### 💥 3.3 Fuzzing
Fuzzed the device’s HTTP API to test input handling and potential buffer overflows or misbehaviors:
- Crafted fuzzing scripts in Python using `requests` and `itertools`
- Automated fuzzing via Burp Suite Intruder with payloads targeting parameters like `cmnd`, `user`, and `password`
- Monitored device stability, reboots, or HTTP error responses

### 🧬 3.4 Static Firmware Analysis
Examined the contents of the firmware image to identify hardcoded secrets, API structure, and file system configuration:
- Used `binwalk` to extract the file system
- Parsed configuration files for default credentials, API keys, and MQTT broker settings
- Inspected scripts and binaries using `strings`, `grep`, and a hex editor

### 🧷 3.5 Hardware Interface Testing
Interacted with the device through its UART debug interface:
- Connected to UART pins via CP2102 USB-to-serial adapter (3.3V)
- Captured boot logs to identify debug info and system services
- Gained shell access (when available) to manually trigger commands and observe logs

---

## 4. Tools & Utilities
| Tool | Purpose |
|------|---------|
| `nmap` | Port scanning and service detection |
| `tcpdump` | Packet capture and traffic analysis |
| `Burp Suite` | HTTP testing and fuzzing |
| `curl`, `Postman` | Manual API probing |
| `binwalk` | Firmware unpacking and extraction |
| `Python` + `requests` | Scripting test automation |
| `CP2102 UART Adapter` | Serial console access |
| `Tasmota` | Custom firmware for controlled testing |

---

## 5. Limitations & Ethics
- Firmware modification was done with full consent on a lab-owned device.
- All attacks simulated were contained to a private network.
- No internet-facing systems were targeted.
- Efforts were made to follow responsible disclosure guidelines if new vulnerabilities were identified.

---

## 6. Summary
The combination of blackbox probing, whitebox firmware access, fuzzing, and physical hardware interfacing provided a comprehensive view of the Sonoff S31's attack surface. This multi-faceted methodology allowed for both broad vulnerability discovery and deep insight into firmware and device-level security behaviors.
