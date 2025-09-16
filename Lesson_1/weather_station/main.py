import dht
import machine
import time

d = dht.DHT22(machine.Pin(15))

while True:
    d.measure()
    humidity = d.humidity()
    temperature = d.temperature()
    print(f"Temperature: {temperature}")
    print(f"Humidity: {humidity}")
    time.sleep(3)
