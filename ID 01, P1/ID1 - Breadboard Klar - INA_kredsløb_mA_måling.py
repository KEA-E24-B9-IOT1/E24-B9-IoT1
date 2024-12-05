from machine import Pin, I2C
import time
from ina219_lib import INA219

# Denne kode er udviklet til Breadboard og ikke Educaboard

i2c = I2C(scl=Pin(18), sda=Pin(19), freq=400000)

ina = INA219(i2c)

while True:
    current = ina.get_current()  # Hent den aktuelle strøm (i mA)
    print("Strømforbrug (mA): ", current)
    time.sleep(1)
