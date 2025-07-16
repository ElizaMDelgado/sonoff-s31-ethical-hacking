# 🔐 User-Level Fixes for Sonoff S31 (Tasmota)

This guide shows how to protect your Sonoff S31 smart plug running Tasmota against the vulnerabilities identified in this project.

## ✅ Step 1: Enable Web UI Authentication

1. Open the Tasmota Web UI (type in your Sonoffs S31 IP address in a browser) 
2. Go to **Configuration → Configure Other**
3. Set a strong **Web Admin Password**
4. Click Save

OR via Console:
```bash
SetOption13 1
```

## Step 2: Disable MQTT (If Not Needed)

In console 
```bash
MqttHost 0.0.0.0
MqttUser ""
MqttPassword ""
SetOption3 1   # Disable MQTT enable/disable toggle via GUI
SetOption13 1  # Require authentication for web and command access

```

##  Step 3: Disable OTA (If Not Needed)
In console 
```bash
SetOption78 1
```

## Step 4: Secure Your Network
Move the plug to a dedicated IoT VLAN or guest network

Block port 80/1883 for LAN-wide access using firewall rules

Only allow access from trusted admin IPs
