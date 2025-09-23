import network
import time
import urequests
import dht
from machine import Pin

ssid = 'Wokwi-GUEST'
password = ''
sensor = dht.DHT22(Pin(15))

THINGSPEAK_API_KEY = 'XXXXXXXXXXXXXXXXXX'  # Replace with your ThingSpeak API key
THINGSPEAK_URL = 'https://api.thingspeak.com/update'  # ThingSpeak endpoint

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

print("Connecting to Wi-Fi", end="")
while not wlan.isconnected():
    print(".", end="")
    time.sleep(0.5)

print("\nConnected!")
print("IP address:", wlan.ifconfig()[0])

def send_to_backend(temp):
    if temp is None:
        print("No temperature send.")
        return
    try:
        response = urequests.post(THINGSPEAK_URL, data='api_key={}&field1={}'.format(THINGSPEAK_API_KEY, temp), headers={'Content-Type': 'application/x-www-form-urlencoded'})
        print("ThingSpeak response:", response.text)
        response.close()
    except Exception as e:
        print("Failed to send data:", e)

while True:
    try:
        sensor.measure()
        temperature = sensor.temperature()
        print("Temperature:", temperature, "°C")
        send_to_backend(temperature)
    except Exception as e:
        print("Error reading sensor or sending data:", e)

    time.sleep(15)