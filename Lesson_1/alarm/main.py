import time
import machine

pir = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin("LED", machine.Pin.OUT)

def pir_handler(pin):
    print("Liikettä havaittu!")
    for i in range(20):
        led.toggle()
        time.sleep(0.5)

pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)