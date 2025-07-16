# 🔐 Credential Hardening for Sonoff S31 (Tasmota)

Weak or missing authentication is one of the most common and dangerous misconfigurations found in smart home devices. This guide explains how to harden credentials on the Sonoff S31 running Tasmota to prevent unauthorized access, configuration tampering, and data leakage.

---

## 🚨 Why This Matters

By default, Tasmota allows unauthenticated access to the web interface and its powerful API endpoints (`/cm`). Without a strong password in place, attackers on the local network can:

- Toggle power or restart the plug
- Change MQTT broker settings
- Redirect OTA updates to malicious firmware
- Extract network configuration and device identity

---

##  Step-by-Step: Secure the Web Interface

### 1. Set a Strong Web Admin Password

- Navigate to your Tasmota device in a browser  
  e.g., `http://172.21.56.214`
- Go to: **Configuration → Configure Other**
- Set a strong password in the **Web Admin Password** field
- Click **Save**

🔑 Use a password manager to generate a unique, complex password.

---

### 2. Require Login for API Access

Open the Tasmota **Console** tab and enter:
```bash
SetOption13 1
```
