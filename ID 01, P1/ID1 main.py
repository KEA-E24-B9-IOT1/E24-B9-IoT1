""" 
Denne fil er til ID 1.
Krav er som følgende:
Løsningen skal køre på batteri og skal som minimum kunne fungere i en time. 
Samtidig skal batteristatus, resterende kapacitet i procent, vises.
"""

from adc_sub import ADC_substitute # Skal erstattes af INA219 modul
from ina219_lib import INA219
from time import sleep
import backend

# CONFIGURATION
pin_ina_scl=backend.pin_ina_scl # INA 219 serial clock line
pin_adc_sda=backend.pin_ina_sda # INA 219 serial data line


# OBJECTS
# Vil vi instantiere i filen?
i2c=I2C(scl=Pin(pin_ina_scl),sda=Pin(pin_ina_sda),freq=400000) # I2C instantiering af ina-pins
# Eller vil vi hente objektet fra anden fil?
ina219=backend.ina219
# ina219.set_calibration_32V_2A() # Følsomhed, kan ændres


# FUNCTIONS
def batt_percentage():
    voltage=ina219.get_bus_voltage()
    batt_percentage=((voltage-6)/(8.4-6))*100
    return batt_percentage

while True:
    lcd.move_to(0,0)
    lcd.clear()
    lcd.putstr(f"Batteriprocent: {batt_percentage()}")
    lcd.move_to(0,2)
    lcd.putstr(f"restlevetid: {3600/ina219.get_current()} timer")
    print(batt_percentage())
    sleep(0.5)
