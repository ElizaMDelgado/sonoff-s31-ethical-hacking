
@echo off
curl "http://192.168.1.113/cm?cmnd=FriendlyName1%20ExploitPlug"
curl "http://192.168.1.113/cm?cmnd=Power%20Off"
curl "http://192.168.1.113/cm?cmnd=Delay%205"
curl "http://192.168.1.113/cm?cmnd=Power%20On"
curl "http://192.168.1.113/cm?cmnd=Status%200"
curl "http://192.168.1.113/cm?cmnd=Status%202"
curl "http://192.168.1.113/cm?cmnd=Status%205"
curl "http://192.168.1.113/cm?cmnd=Status%208"
curl "http://192.168.1.113/cm?cmnd=Info"
curl "http://192.168.1.113/cm?cmnd=Voltage"
curl "http://192.168.1.113/cm?cmnd=Current"
curl "http://192.168.1.113/cm?cmnd=Power"
curl "http://192.168.1.113/cm?cmnd=EnergyToday"
curl "http://192.168.1.113/cm?cmnd=EnergyTotal"
curl "http://192.168.1.113/cm?cmnd=Restart%201"
pause
