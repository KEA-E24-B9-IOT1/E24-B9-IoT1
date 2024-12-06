""" 
Denne fil er til ID 1.
Krav er som følgende:
Løsningen skal køre på batteri og skal som minimum kunne fungere i en time. 
Samtidig skal batteristatus, resterende kapacitet i procent, vises.
"""

from adc_sub import ADC_substitute # Skal erstattes af INA219 modul
from time import sleep
import hardware_pins_config as hw

# CONFIGURATION
pin_ina_scl=hw.pin_ina_scl # INA 219serial clock line
pin_adc_sda=hw.pin_ina_sda # INA219 serial data line

# OBJECTS
adc=ADC_substitute(34) # Skal erstattes 
lcd=hw.lcd # Hent lcd fra hw-modul

def batt_percentage():
    voltage=adc.read_voltage()*2
    batt_percentage=((voltage-3)/(4.2-3.0))*100
    return batt_percentage

while True:
    lcd.move_to(0,0)
    lcd.clear()
    lcd.putstr(f"Batteriprocent: {batt_percentage()}")
    print(batt_percentage())
    sleep(0.5)
