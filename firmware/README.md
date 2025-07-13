#  Firmware Folder

## Script Descriptions

### `run_s31_tests.bat`
This script uses `curl` to:
- Toggle power and LED states
- Restart the device
- Change MQTT configuration (host, user, password, etc.)
- Modify the device's name and OTA URL
- Collect status information
- Log everything to `s31_test_log.txt`

🔍 *Purpose*: To validate API behavior and test for improper authentication, config injection, or persistence of changes.

---

### `tasmota_commands.bat`
This script sends:
- Additional status and power commands
- Requests for sensor readings (e.g., `Voltage`, `Current`, `EnergyToday`)
- Friendly name changes and restart triggers

🔍 *Purpose*: Acts as a replay or stress test against common Tasmota features to observe behavior under repeated commands.

---

## ⚠️ Note on Ethics

These scripts were tested on a personal Sonoff S31 device within a secure, local network.  
They should **never** be used without permission on production or third-party devices.

---

