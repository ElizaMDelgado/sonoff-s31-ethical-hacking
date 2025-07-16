#  Summary of Mitigations

This file lists all recommended mitigations for the vulnerabilities discovered during testing of the Sonoff S31 smart plug running Tasmota.

---

## F01: Unauthenticated Local API Access

**Fixes:**
- Enable authentication via `SetOption13 1`
- Set a strong Web Admin password
- Restrict port 80 access to trusted admin IPs using firewall rules

---

## F02: MQTT Configuration Injection

**Fixes:**
- Clear MQTT credentials and disable unused MQTT features:
  ```bash
  MqttHost 0.0.0.0
  MqttUser ""
  MqttPassword ""
  SetOption3 1
  ```

## F03: OTA URL Hijacking

**Fixes:**
 - Disable OTA if not used:
  ```bash
  SetOption78 1
 ```
- Do not allow external OTA URLs

- Use a firewall to block access to unauthorized firmware sources

## F04: Information Leakage via Status API

**Fixes:**
Enable authentication for /cm commands:
  ```bash
SetOption13 1
 ```
- Limit who can access /cm?cmnd=Status or /Info using IP filtering

- Isolate IoT devices on a guest or VLAN segment

## F05: UART Shell Access
**Fixes:**
- Disable serial console in Tasmota (if not needed)

- Physically secure the device

- Cover UART pads with epoxy if the device is in a production environment

## Network-Wide Recommendations
- Use DHCP reservation or static IP to avoid address-based spoofing

- Segment IoT devices on a dedicated VLAN or guest Wi-Fi

- Monitor device logs for unusual access or reboots

- Regularly update Tasmota firmware with official, trusted builds

## Use in Combination
These mitigations are most effective when combined into a layered defense strategy:

  - Firmware-level security (Tasmota config)

  - Credential and API hardening

  -  Network segmentation and access control

  - Monitoring and detection
