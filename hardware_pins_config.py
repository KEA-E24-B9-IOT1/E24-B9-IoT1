"""
Denne fil er til vores hardware og hvilke pins de er tilsluttet,
så der er et samlet overblik.
Så kan vi evt. også importere vores pins herfra.
"""

dht11_pin = 15 # 3.3V

pin_buzzer = 14 # Jumpes JP1-SCK <-> JP6-GP6 eller via Port Exp.

pin_adc_scl = 18
pin_adc_sda = 19


pin_adc = 39 # IKKE PIN 34!!! DEN ER TILKOBLET POTENTIOMETER!!!

pin_blinker_left = 26
pin_button_left = 4

pin_blinker_right = 12 # Jumpes JP1-MISO <-> JP6-GP2 eller via Port Exp.
pin_button_right = 0

pin_lcd_rs        = 27
pin_lcd_enable    = 25
pin_lcd_db4       = 33
pin_lcd_db5       = 32
pin_lcd_db6       = 21
pin_lcd_db7       = 22
pin_lcd_contrast  = 23
lcd_num_lines     =  4
lcd_num_columns   = 20

pin_gps_port = 2                               # ESP32 UART port, Educaboard ESP32 default UART port
gps_speed = 9600                           # UART speed, defauls u-blox speed


