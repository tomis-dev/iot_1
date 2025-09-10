import machine
import time
time.sleep(0.1) # Wait for USB to become ready

led = machine.Pin(15, machine.Pin.OUT)

while True:
    led.toggle()
    time.sleep(1)
