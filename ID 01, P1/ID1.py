""" 
Denne fil er til ID 1.
Krav er som følgende:
Løsningen skal køre på batteri og skal som minimum kunne fungere i en time. 
Samtidig skal batteristatus, resterende kapacitet i procent, vises.
"""

from machine import Pin, ADC
from gpio_lcd import GpioLcd
from adc_sub import ADC_substitute
from time import sleep

# CONFIGURATION
pin_adc=34
lcd_rs_pin=27
lcd_enable_pin=25
lcd_d4_pin=33
lcd_d5_pin=32
lcd_d6_pin=21
lcd_d7_pin=22
lcd_num_lines=4
lcd_num_columns=20

# OBJECTS
adc=ADC_substitute(pin_adc)
lcd=GpioLcd(
    Pin(lcd_rs_pin),
    Pin(lcd_enable_pin),
    Pin(lcd_d4_pin),
    Pin(lcd_d5_pin),
    Pin(lcd_d6_pin),
    Pin(lcd_d7_pin),
    lcd_num_lines,
    lcd_num_columns)

def batt_percentage():
    voltage=adc.read_voltage()*2
    batt_percentage=((voltage-3)/(4.2-3.0))*100
    return batt_percentage

while True:
#     lcd.move_to(0,0)
#     lcd.clear()
#     lcd.putstr(f"Batteriprocent: {batt_percentage()}")
    print(batt_percentage())
    sleep(0.5)
