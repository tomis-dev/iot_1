import network
import urequests
import time
from machine import Pin, I2C
import dht
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import config

ssid = "Wokwi-GUEST"
password = ""

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    pass

print("Connected:", wlan.ifconfig())

sensor = dht.DHT22(Pin(15))

THINGSPEAK_API_KEY = config.THINGSPEAK_KEY
THINGSPEAK_URL = "https://api.thingspeak.com/update"

MIN_TEMP = 15
MAX_TEMP = 28
MIN_HUM = 35
MAX_HUM = 65

I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    
    alert = 0
    if temp < MIN_TEMP or temp > MAX_TEMP or hum < MIN_HUM or hum > MAX_HUM:
        alert = 1
    lcd.clear()
    lcd.putstr(f"Temp: {temp:.1f}C")
    lcd.move_to(0, 1)
    lcd.putstr(f"Hum: {hum:.1f}%")

    if alert:
        lcd.move_to(10, 0)
        lcd.putstr("ALRT")

    response = urequests.get(
        f"{THINGSPEAK_URL}?api_key={THINGSPEAK_API_KEY}&field1={temp}&field2={hum}&field3={alert}"
    )
    print("Sent:", temp, hum, alert, response.text)
    response.close()
    
    time.sleep(20)