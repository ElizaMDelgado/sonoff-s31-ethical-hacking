# 🌐 Network-Level Fixes for Sonoff S31

This guide explains how to reduce the attack surface of the Sonoff S31 smart plug using router-level and firewall protections. These fixes are especially helpful in situations where:

- Firmware vulnerabilities exist
- Authentication is not enabled
- You want defense-in-depth at the network layer

---

## Step 1: Isolate the Plug on a VLAN or Guest Network

If your router supports VLANs or Guest Wi-Fi:

- Move the plug to a dedicated **IoT VLAN** or **guest network**
- Block communication between devices on that VLAN
- Only allow outbound access to:
  - MQTT broker (if used)
  - NTP (UDP 123)
  - OTA server (if updates are required)

---

## Step 2: Block Internal Access from Other Devices

Use your router’s firewall or access control features to block:

- Incoming connections to port `80` (Tasmota Web UI)
- Incoming connections to port `1883` (MQTT)
- Any LAN-wide discovery if not needed

Example for blocking port 80:
```bash
iptables -A INPUT -p tcp --dport 80 -s 192.168.1.0/24 -j DROP
```
##  Step 3: Use Static IP or DHCP Reservation

To prevent the IP address from changing (which can break scripts or allow IP spoofing):

 - Reserve a static IP for the Sonoff S31 in your router’s DHCP settings

 - Or configure a static IP inside Tasmota

A stable IP address allows you to create precise firewall rules, enforce access control, and ensure your monitoring tools or automation scripts always target the correct device. Without a static IP or DHCP reservation, a reboot or network reconfiguration could assign the plug a new address  breaking your protections or making it difficult to detect abnormal activity. Reserving an IP via your router ensures consistent, traceable behavior and prevents other devices from spoofing or stealing that address.


## Step 4: Limit Who Can Access the Plug

Only allow your admin machine to access the plug
Block everyone else by MAC/IP using router ACLs or IP filtering


## Summary

These firewall and isolation techniques help:

  -Prevent attacks from other LAN devices

  -Lock down unauthenticated interfaces

  -Maintain secure, stable device behavior even if firmware has flaws

Use network security as your second layer of defense.


