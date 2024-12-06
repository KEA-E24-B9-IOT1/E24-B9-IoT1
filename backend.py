"""
Denne fil er til vores hardware og hvilke pins de er tilsluttet,
så der er et samlet overblik.
Så kan vi evt. også importere vores pins herfra.
"""
import dht

from gpio_lcd import GpioLcd
from machine import Pin, UART, I2C
from gps_simple import GPS_SIMPLE
from ina219_lib import INA219


########## TEMPLATE
#### NAVN
# Pins


# Instantiering


# Funktioner



#### dht11
# Pins
pin_dht11=None # MANGLER!

# Instantiering
# pin=Pin(pin_dht11) # 
# dht11=dht.DHT11(pin)

# Funktioner
def dht11_temp():
    """DHT11 measure temp in deg C,
    as humidity is not needed."""
    dht11.measure()
    tempC=dht11.temperature()
    return tempC


#### GPS
# Pins
## DO NOT MESS WITH GPS!
pin_gps_port = 2 # ESP32 UART port, Educaboard ESP32 default UART port
pin_gps_pps = 5
pin_gps_tx = 16
pin_gps_rx = 17
gps_speed=9600

# Instantiering
uart=UART(pin_gps_port,gps_speed) # Opsæt uart config til gps'en
gps=GPS_SIMPLE(uart) # Opsæt GPS objektet


#### LCD
# Pins
pin_lcd_rs        = 27
pin_lcd_enable    = 25
pin_lcd_db4       = 33
pin_lcd_db5       = 32
pin_lcd_db6       = 21
pin_lcd_db7       = 22
pin_lcd_contrast  = 23
lcd_num_lines     =  4
lcd_num_columns   = 20

# Instantiation
lcd=GpioLcd(
    rs_pin=Pin(pin_lcd_rs),
    enable_pin=Pin(pin_lcd_enable),
    d4_pin=Pin(pin_lcd_db4),
    d5_pin=Pin(pin_lcd_db5),
    d6_pin=Pin(pin_lcd_db6),
    d7_pin=Pin(pin_lcd_db7),
    num_lines=lcd_num_lines,
    num_columns=lcd_num_columns)


# Funktioner
def display(kol,linj,tekst):
    """Indsæt linje, kolonne og tekst, for hvad der skal vises på display"""
    if isinstance(tekst,str):
        lcd.move_to(kol,linj)
        lcd.putstr(" "*len(tekst))
        lcd.move_to(kol,linj)
        lcd.putstr(str(tekst))
    else:
        print("3rd input has to be a string.")

#### INA219
# Pins
pin_ina_scl = 18 # SCL line
pin_ina_sda = 19 # SDA line

# Instantiering
# i2c=I2C(scl=Pin(pin_ina_scl),sda=Pin(pin_ina_sda),freq=400000) # I2C instantiering af ina-pins
# ina219=INA219(i2c) #  instantiering af ina219 med I2C

# Funktioner
def batt_percentage():
    """adc through ina219, returns batt% from 3.0-4.2V
    Li-ion batt."""
    voltage=adc.read_voltage()*2 # *2 for a proper reading, *3 for simulated batteri
    batt_percentage=((voltage-3)/(4.2-3.0))*100
    return batt_percentage