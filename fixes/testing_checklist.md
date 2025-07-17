# ✅ Security Testing Checklist for Sonoff S31 (Tasmota)

This checklist verifies that all recommended hardening measures have been applied correctly and are functioning as intended. Use this as a final validation step after applying the fixes documented in this project.

---

##  Credential Protection

| Test Description                                        | Expected Result           | Pass |
|---------------------------------------------------------|----------------------------|------|
| Web interface requires login                            | Prompts for username/password | [ ]  |
| API commands fail without authentication (`curl`)       | Returns `401 Unauthorized`    | [ ]  |
| API commands succeed with correct `--user` credentials  | Returns expected JSON         | [ ]  |
| Web password cleared during reset                       | Web login no longer required | [ ]  |

---

##  MQTT Injection Mitigation

| Test Description                                        | Expected Result            | Pass |
|---------------------------------------------------------|-----------------------------|------|
| Can’t change `MqttHost` without auth                    | `401 Unauthorized` or failure | [ ]  |
| `MqttHost` returns default or cleared value             | `0.0.0.0`                     | [ ]  |
| MQTT connection rejected if no broker is set            | No connection or logs show failure | [ ]  |

---

##  OTA Hijack Mitigation

| Test Description                                        | Expected Result            | Pass |
|---------------------------------------------------------|-----------------------------|------|
| Setting `OtaUrl` requires authentication                | Returns `401 Unauthorized` | [ ]  |
| OTA updates disabled with `SetOption78 1`               | OTA URL change has no effect | [ ]  |

---

##  Info Leakage / API Access

| Test Description                                        | Expected Result             | Pass |
|---------------------------------------------------------|------------------------------|------|
| `Status 11` and `Info` fail without login               | `401 Unauthorized`           | [ ]  |
| Console shows blocked command attempts                  | Logs rejected access or unknown IPs | [ ]  |
| Access to `Status` commands only with credentials       | Works with `--user` only     | [ ]  |

---

##  Network Restrictions

| Test Description                                        | Expected Result              | Pass |
|---------------------------------------------------------|-------------------------------|------|
| Port 80 blocked from untrusted IPs                      | Request dropped or denied     | [ ]  |
| Port 1883 (MQTT) only accessible from trusted devices   | Denied or timeout from others | [ ]  |
| VLAN or guest network separation confirmed              | Device not reachable across segments | [ ]  |

---

##  Final Configuration Review

| Check                                                   | Expected Setting             | Pass |
|----------------------------------------------------------|-------------------------------|------|
| `SetOption13` is set to `1`                              | Requires login                | [ ]  |
| `SetOption78` is set to `1`                              | OTA disabled                  | [ ]  |
| `MqttHost`, `MqttUser`, `MqttPassword` cleared           | All blank                     | [ ]  |
| Web Admin password is strong and unique                  | ✅ Confirmed                  | [ ]  |

---

##  How to Use This

- Use the checklist as part of your hardening verification process
- Include screenshots if documenting results in a report or presentation
- Share with others who may want to secure their own smart plugs

