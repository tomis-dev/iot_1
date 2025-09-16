import time
import machine
time.sleep(0.1) # Wait for USB to become ready


button = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
led = machine.Pin(18, machine.Pin.OUT)
print("Program starting...")
while True:
    if button.value() == 0:
        led.value(1)
    else:
        led.value(0)
