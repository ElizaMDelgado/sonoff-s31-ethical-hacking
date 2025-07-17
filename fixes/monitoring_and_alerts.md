#  Monitoring and Alerts for Sonoff S31 (Tasmota)

Hardening the Sonoff S31 against vulnerabilities is critical, but **monitoring for unauthorized activity** is equally important. This guide provides options for detecting suspicious commands, failed login attempts, and unusual behavior through Tasmota’s own logs, network monitoring, and external tools.

---

##  1. Monitor the Tasmota Console

Tasmota includes a built-in console that logs all received commands and system activity.

###  What to do:
- Open the plug’s web interface → Click **Console**
- Watch for:
  - Unexpected `cmnd` requests
  - Reboots or configuration changes
  - Access from unknown IP addresses

###  Example Log Entries:
```bash
14:20:03 CMD: Power Off
14:20:04 MQT: stat/sonoff/RESULT = {"POWER":"OFF"}
14:21:08 HTTP: Unknown command from 10.149.2.33
```

##  2. Monitor Traffic with Your Router or IDS

If your router supports logs or integrates with a firewall like **pfSense**, **OpenWRT**, or **Suricata**, you can track:

- Unusual requests to port `80`, `1883`, or OTA URLs
- Repeated curl attempts or brute-force probes
- New IPs attempting connections to the device

---

## 3. Enable MQTT Telemetry (Optional)

```bash
TelePeriod 30
```
- Sends regular status messages

- Monitor via MQTT broker or log collector like Node-RED, Mosquitto, or Home Assistant

- Watch for unexpected command topics (cmnd/ or stat/ activity)

## Track Uptime and Unexpected Resets
Frequent reboots can indicate attacks or crashes from malformed input.
Check uptime via:
```bash
curl "http://[plug_ip]/cm?cmnd=Status%2011"
```
Or in the web console:
```bash
00:13:04 APP: Uptime 0T00:13:04
```

## 5. Optional Alerts Using External Tools
If you want to automate detection:

- Use Node-RED to parse MQTT or HTTP logs and send alerts (email, Discord, etc.)

- Use log monitoring tools like Graylog, Grafana, or Elasticsearch
