import time
import machine

button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
green = machine.Pin(13, machine.Pin.OUT)
yellow = machine.Pin(14, machine.Pin.OUT)
red = machine.Pin(15, machine.Pin.OUT)
buzzer = machine.Pin(12, machine.Pin.OUT)
button_pressed_flag = False
time.sleep(0.1) # Wait for USB to become ready

def all_off():
    green.value(0)
    yellow.value(0)
    red.value(0)
    buzzer.value(0)


def button_pressed(pin):
    global button_pressed_flag
    button_pressed_flag = True

button.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_pressed)

while True:
    print("Silmukka alkaa")
    if button_pressed_flag:
        print("Nappia painettu")
        all_off()
        buzzer.value(1)
        red.value(1)
        time.sleep(4)
        buzzer.value(0)
        red.value(0)
        button_pressed_flag = False
        continue
    green.value(1)
    time.sleep(2)
    green.value(0)
    yellow.value(1)
    time.sleep(2)
    yellow.value(0)
    red.value(1)
    time.sleep(2)
    red.value(0)
