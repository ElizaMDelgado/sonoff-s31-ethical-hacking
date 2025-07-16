# 🔥 Firewall-Based Restrictions for Sonoff S31 (Tasmota)

Even when Tasmota is hardened with a password, placing additional restrictions at the network level helps reduce attack surface and prevents unauthorized devices from interacting with the smart plug.

This guide shows how to use firewall rules to protect the Sonoff S31 on your home or lab network.

---

## Goals

- Block unauthorized access to the plug’s web UI (port 80)
- Prevent remote API commands over HTTP
- Restrict MQTT traffic (port 1883) to trusted systems
- Isolate the plug from general LAN traffic using IP filters

---

##  Common Ports to Restrict

| Port | Protocol | Purpose                 |
|------|----------|-------------------------|
| 80   | TCP      | Web UI + API commands   |
| 1883 | TCP      | MQTT broker (if enabled)|
| 8266 | TCP      | OTA updates (optional)  |

---

## 🛡UFW (Linux Firewall) Example

Allow only one admin IP (e.g., 10.149.2.100) to access the plug:

```bash
# Default: deny incoming traffic
sudo ufw default deny incoming

# Allow admin machine to connect to plug on port 80
sudo ufw allow from 10.149.2.100 to 10.149.2.214 port 80

# Block everyone else
sudo ufw deny to 10.149.2.214 port 80
```

## Summary 
Firewall-based protections are critical for defense-in-depth:

  - Block network-wide curl/API abuse

  - Ensure only trusted devices can talk to the plug

  - Prevent fallback exploitation even if auth is disabled

Use these restrictions alongside firmware hardening for complete coverage.
