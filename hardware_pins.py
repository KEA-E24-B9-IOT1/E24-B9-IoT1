"""
DETTE SKAL STREAMLINES!!!!!

Denne fil er til vores hardware og hvilke pins de er tilsluttet,
så der er et samlet overblik.
Så kan vi evt. også importere vores pins herfra.
"""
# ID 1
pin_adc=34
lcd_rs_pin=27
lcd_enable_pin=25
lcd_d4_pin=33
lcd_d5_pin=32
lcd_d6_pin=21
lcd_d7_pin=22
lcd_num_lines=4
lcd_num_columns=20


# ID 2
dht11_pin=19
adc_pin=34
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


# ID 3
dht11_pin=19
adc_pin=34
gps_port = 2                               # ESP32 UART port, Educaboard ESP32 default UART port
gps_speed = 9600                           # UART speed, defauls u-blox speed


# ID 4
##### PINS
# ESP32 UART port, Educaboard ESP32 default UART port
gps_port = 2

##### CONFIGURATIONS
# UART speed, defauls u-blox speed
gps_speed = 9600

# ID 6
n = 12 #Number of NeoPixels
# np = NeoPixel(Pin(16, Pin.OUT), n) #np Object on Pin 16

# i2c = I2C(0) #I2C init. Pin 18 SCL, Pin 19 SDA
# imu = MPU6050(i2c) #MPU

# ID 7


# ID 8


# ID 9
pin_buzzer=14 # Jumpes JP1-SCK <-> JP6-GP6 eller via Port Exp.

# ID 11
pin_blinker_left=26
pin_button_left=4

pin_blinker_right=12 # Jumpes JP1-MISO <-> JP6-GP2 eller via Port Exp.
pin_button_right=0
