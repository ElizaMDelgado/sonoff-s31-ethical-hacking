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

## Recommendation
- Enable authentication for web and API access: SetOption13 1 in the Tasmota web console
  ```bash
  SetOption13 1
  ```

- Avoid exposing Tasmota to the public internet

- Place the plug on a segmented IoT VLAN to limit who can access these endpoints

##  Additional Recommendations

- Require authentication for all API and web access using `SetOption13 1`
- Isolate the plug on a separate VLAN or guest Wi-Fi network
- Block port 80 from untrusted IP addresses at the router/firewall
- Disable MQTT discovery using `SetOption19 0` in the Tasmota web console
   ```bash
   SetOption19 0
  ```
   
- Monitor device logs for unexpected IP requests
