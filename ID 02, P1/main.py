##### IMPORTS
from time import sleep
from machine import reset, UART, Pin
import gc
from gps_simple import GPS_SIMPLE
import dht
from adc_sub import ADC_substitute
from gpio_lcd import GpioLcd
import math


##### PINS
dht11_pin=19
adc_pin=34
# ESP32 UART port, Educaboard ESP32 default UART port
gps_port = 2
pin_lcd_rs        = 27
pin_lcd_enable    = 25
pin_lcd_db4       = 33
pin_lcd_db5       = 32
pin_lcd_db6       = 21
pin_lcd_db7       = 22
pin_lcd_contrast  = 23
lcd_num_lines     =  4
lcd_num_columns   = 20


##### CONFIGURATIONS
# UART speed, defauls u-blox speed
gps_speed = 9600


##### OBJECTS
uart = UART(gps_port, gps_speed)
gps = GPS_SIMPLE(uart)
adc=ADC_substitute(adc_pin)
dht11=dht.DHT11(Pin(dht11_pin))
lcd=GpioLcd(rs_pin=Pin(pin_lcd_rs),
    enable_pin=Pin(pin_lcd_enable),
    d4_pin=Pin(pin_lcd_db4),
    d5_pin=Pin(pin_lcd_db5),
    d6_pin=Pin(pin_lcd_db6),
    d7_pin=Pin(pin_lcd_db7),
    num_lines=lcd_num_lines,
    num_columns=lcd_num_columns)

##### FUNCTIONS

def dht11_temp():
    """DHT11 measure temp in deg C,
    as humidity is not needed."""
    dht11.measure()
    tempC=dht11.temperature()
    return tempC

def batt_percentage():
    """adc through ina219, returns batt% from 3.0-4.2V
    Li-ion batt."""
    voltage=adc.read_voltage()*2 # *2 for a proper reading, *3 for simulated batteri
    batt_percentage=((voltage-3)/(4.2-3.0))*100
    return batt_percentage


##### PROGRAM
while True:
    try:
        print(f"free memory: {gc.mem_free()}") # monitor memory left
        if gc.mem_free() < 2000:          # free memory if below 2000 bytes left
            print("Garbage collected!")
            gc.collect()                  # free memory 
        if gps.receive_nmea_data(): # If gps data is received
            data={"La":gps.get_latitude(),"Lo":gps.get_longitude(),"Course":gps.get_course(),"Speed":gps.get_speed(),"Temp":dht11_temp(),"Batt%":batt_percentage()}
            print(data)
            lcd.move_to(0,0)
            lcd.putstr(" "*10)
            lcd.move_to(0,0)
            lcd.putstr(f"Batt%:{int(batt_percentage())} Temp:{dht11_temp()}")
            lcd.move_to(0,1)
            lcd.putstr(" "*10)
            lcd.move_to(0,1)
            lcd.putstr(f"La:{gps.get_latitude()}")
            lcd.move_to(0,2)
            lcd.putstr(" "*10)
            lcd.move_to(0,2)
            lcd.putstr(f"Lo:{gps.get_longitude()}")
            lcd.move_to(0,3)
            lcd.putstr(" "*10)
            lcd.move_to(0,3)
            # Lav Course om til at give kardinalværdier i stedet for tal
            lcd.putstr(f"Speed:{math.ceil(gps.get_speed())} Course:{gps.get_course()}")
        sleep(1)                          # send telemetry once every second
    except KeyboardInterrupt:
        print("Disconnected!")
        reset()                           # reset ESP32