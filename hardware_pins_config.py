"""
Denne fil er til vores hardware og hvilke pins de er tilsluttet,
så der er et samlet overblik.
Så kan vi evt. også importere vores pins herfra.
"""
from gpio_lcd import GpioLcd
from machine import Pin, UART, Pin
from gps_simple import GPS_SIMPLE

# DO NOT MESS WITH GPS!

pin_gps_port = 2 # ESP32 UART port, Educaboard ESP32 default UART port
pin_gps_pps = 5
pin_gps_tx = 16
pin_gps_rx = 17


pin_buzzer = 14 # Jumpes JP1-SCK <-> JP6-GP6 eller via Port Exp.

pin_dht11 = # NEED TO SET THIS UP

pin_relay = # NEED TO SET THIS UP!

pin_ina_scl = 18
pin_ina_sda = 19

pin_blinker_left = 26
pin_button_left = 4

pin_blinker_right = 12 # Jumpes JP1-MISO <-> JP6-GP2 eller via Port Exp.
pin_button_right = 0

### LCD
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
    Pin(pin_lcd_rs),
    Pin(pin_lcd_enable),
    Pin(pin_lcd_db4),
    Pin(pin_lcd_db5),
    Pin(pin_lcd_db6),
    Pin(pin_lcd_db7),
    lcd_num_lines,
    lcd_num_columns)