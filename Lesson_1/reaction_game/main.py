import utime
import machine
import urandom


button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)
timer_start = 0

def button_handler(pin):
    button.irq(handler=None)
    reaction_time = utime.ticks_diff(utime.ticks_ms(), timer_start)
    print("Reaktioaikasi: {} ms".format(reaction_time))



print("Valmistaudu...")
led.value(1)
utime.sleep(urandom.getrandbits(3) + 2)
led.value(0)
timer_start = utime.ticks_ms()
print("Paina nappia!")


button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)