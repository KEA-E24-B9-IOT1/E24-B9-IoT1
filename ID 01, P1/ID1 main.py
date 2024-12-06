""" 
Denne fil er til ID 1.
Krav er som følgende:
Løsningen skal køre på batteri og skal som minimum kunne fungere i en time. 
Samtidig skal batteristatus, resterende kapacitet i procent, vises.
"""

from adc_sub import ADC_substitute # Skal erstattes af INA219 modul
from ina219_lib import INA219
from time import sleep
import hardware_pins_config as hw

# CONFIGURATION
pin_ina_scl=hw.pin_ina_scl # INA 219 serial clock line
pin_adc_sda=hw.pin_ina_sda # INA 219 serial data line


# OBJECTS
# Vil vi instantiere i filen?
i2c=I2C(scl=Pin(pin_ina_scl),sda=Pin(pin_ina_sda),freq=400000) # I2C instantiering af ina-pins
# Eller vil vi hente objektet fra anden fil?
ina219=hw.ina219
# ina219.set_calibration_16V_400mA() # Følsomhed, kan ændres


# FUNCTIONS
def batt_percentage():
    voltage=ina219.get_bus_voltage()*2
    batt_percentage=((voltage-3)/(4.2-3.0))*100
    return batt_percentage

while True:
    lcd.move_to(0,0)
    lcd.clear()
    lcd.putstr(f"Batteriprocent: {batt_percentage()}")
    lcd.move_to(0,2)
    lcd.putstr(f"restlevetid: {3600/ina219.get_current()} timer")
    print(batt_percentage())
    sleep(0.5)
