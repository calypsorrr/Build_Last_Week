from network import WLAN
import machine
import pycom
import time

def wifi_connect():
    pycom.heartbeat(False)
    wlan = WLAN(mode=WLAN.STA)
    wlan.connect(ssid="IoT", auth=(WLAN.WPA2, 'KdGIoT22!'))
    while not wlan.isconnected():
        time.sleep(1)
        pycom.rgbled(0xFF0000)
    print("WiFi connected succesfully")
    pycom.rgbled(0x00FF00)
    time.sleep(2)
    print(wlan.ifconfig())
