"""
Denne fil er til vores hardware og hvilke pins de er tilsluttet,
så der er et samlet overblik.

Der er også tilhørende configs og funktioner.
"""

##### IMPORTS
import dht

from machine import Pin, UART, I2C
from gpio_lcd import GpioLcd
from ina219_lib import INA219
from gps_simple import GPS_SIMPLE
from mpu6050 import MPU6050
from neopixel import NeoPixel
from time import ticks_ms


##### PINS
pin_button_two = 0
pin_button_one = 4
pin_gps_pps = 5 # Don't change
pin_solenoid = 15
pin_gps_tx = 16 # Don't change
pin_gps_rx = 17 # Don't change
pin_scl = 18 # I2C
pin_sda = 19 # I2C
pin_lcd_db6 = 21 # Don't change
pin_lcd_db7 = 22 # Don't change
pin_lcd_contrast = 23 # Don't change
pin_lcd_enable = 25 # Don't change
pin_neoring = 26
pin_lcd_rs = 27 # Don't change
pin_lcd_db5 = 32 # Don't change
pin_lcd_db4 = 33 # Don't change
pin_buzzer = 34
pin_dht11 = 35
pin_neostrip_one = 36
pin_neostrip_two = 39
pin_mpu = None # connect via sda and scl
pin_ina = None # connect via sda and scl


##### CONFIGURATIONS
lcd_num_lines = 4
lcd_num_columns = 20
gps_baudrate = 9600 # u-block default
gps_port = 2 # Don't change


##### OBJECTS
gps=GPS_SIMPLE(UART(gps_port,gps_baudrate)) # 5V
lcd=GpioLcd(rs_pin=Pin(pin_lcd_rs),
            enable_pin=Pin(pin_lcd_enable),
            d4_pin=Pin(pin_lcd_db4),
            d5_pin=Pin(pin_lcd_db5),
            d6_pin=Pin(pin_lcd_db6),
            d7_pin=Pin(pin_lcd_db7),
            num_lines=lcd_num_lines,
            num_columns=lcd_num_columns) # 3.3V

ina=INA219(I2C(scl=Pin(pin_scl),sda=Pin(pin_sda),freq=400000)) # 3.3V

dht11=dht.DHT11(Pin(pin_dht11)) # 3.3V

buzzer_PWM_objekt=PWM(Pin(pin_buzzer,Pin.OUT),freq=1,duty=0) # 3.3V?

imu=MPU6050(I2C(scl=Pin(pin_scl),sda=Pin(pin_sda),freq=400000)) # 3.3V

neoring=NeoPixel(Pin(pin_neoring,Pin.OUT),15)

left_blinker=NeoPixel(Pin(pin_neostrip_one,Pin.OUT),3)

left_button=Pin(pin_button_one,Pin.IN)

right_blinker=NeoPixel(Pin(pin_neostrip_two,Pin.OUT),3)

right_button=Pin(pin_button_two,Pin.IN)


##### FUNCTIONS
def handler_alarm(req_id,method,params):
    """Handler callback to receive RPC from server, to enable or disable alarm"""
    print(f"Response: {req_id}: {method}, params {params}")
    print(params, "params type:", type(params))
    try:
        if method=="Enable alarm":
            if params==True:
                print("Alarm enabled")
                global alarm_enabled=True
            elif params==False:
                print("Alarm disabled")
                global alarm_enabled=False
        if method=="secondCommand":
            print(params.get("command"))
    except TypeError as e:
        print(e)

def dht11_temp():
    """Measure with dht11, return temp in °C"""
    dht11.measure()
    tempC=dht11.temperature()
    return tempC

def ina_voltage():
    """Read voltage from ina"""
    return ina.get_bus_voltage()

def ina_current():
    """Read current from ina"""
    return ina.get_current()

def batt_percentage():
    """Return battery-%, 4.2V is cons. 100%, and 3.0V is considered 0%."""
    voltage=ina_voltage()*2 # Multiply based on circuit voltage divider
    batt_percentage=((voltage-3)/(4.2-3.0))*100 # Return is %-based
    return batt_percentage

def display(col, lin, text):
    """ Insert column, line and text for what to display on LCD."""
    if isinstance(text,str):
        """Check if input is a string"""
        lcd.move_to(col,lin)
        lcd.putstr(" "*len(text))
        lcd.move_to(col,lin)
        lcd.putstr(text)
    else:
        """Display only accepts strings"""
        lcd.clear()
        lcd.move_to(0,0)
        lcd.putstr("Input is not string")
        lcd.move_to(0,1)
        lcd.putstr("Make input string")

def neopixel_clear():
    """Turn off neopixel lights"""
    for i in range(n):
        np[i]=(0,0,0)
    np.write()

def neopixel_flash(r,g,b):
    """Enable flashy lights"""
    for i in range (n):
        np[i]=(r,g,b)
    np.write()

def disable_active_alarm():
    """Disable sound and lights"""
    neopixel_clear()
    buzzer_PWM_objekt.duty(0)

def trigger_alarm(r,g,b):
    """Trigger flashy lights and annoying sounds"""
    neopixel_flash(r,g,b)
    buzzer_PWM_objekt.freq(1023)
    buzzer_PWM_objekt.duty(512)
    # A delay - blocking or non-blocking??
    neopixel_flash(b,g,r)
    buzzer_PWM_objekt.freq(512)
    # A delay - blocking or non-blocking?

def blinker():
    """Function to make a signal light blink"""
    blinker_ticker=ticks_ms()
    if ticks_ms()-blinker_ticker>100:
        i for i in range(3):
            np[i]=(0,50,50)
        np.write()
        i for i in range(3):
            np[i]=(0,0,0)
        np.write()
        blinker_ticker=ticks_ms()
