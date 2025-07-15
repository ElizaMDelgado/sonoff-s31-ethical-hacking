# 🛑 Unauthenticated Local API Access

## 📋 Summary
The Sonoff S31 smart plug running Tasmota version 15.0.1  was found to accept unauthenticated HTTP requests from any device on the same network. This allows an attacker to control the plug or modify settings without requiring a login.

## 🧪 Example Commands
```bash
curl "http://192.168.1.113/cm?cmnd=Power%20Off"
curl "http://192.168.1.113/cm?cmnd=Restart%201"
```
Impact

    Attackers can toggle power to any connected device

    Restart or disable the plug remotely

    Use it as a pivot into other IoT systems
