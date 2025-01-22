"""
Denne fil er til vores hardware og hvilke pins de er tilsluttet,
så der er et samlet overblik.

Der er også tilhørende configs og funktioner.
"""

##### IMPORTS
import dht

from uthingsboard.client import TBDeviceMqttClient
from machine import Pin, UART, I2C, PWM
from gpio_lcd import GpioLcd
from ina219_lib import INA219
from gps_simple import GPS_SIMPLE
from mpu6050 import MPU6050
from neopixel import NeoPixel
from time import ticks_ms


##### PINS
pin_button_left = 36
pin_button_right = 39
PIN_GPS_PPS = 5 # Don't change
pin_solenoid = 15
PIN_GPS_TX = 16 # Don't change
PIN_GPS_RX = 17 # Don't change
pin_scl = 18 # I2C
pin_sda = 19 # I2C
pin_lcd_db6 = 21 # Don't change
pin_lcd_db7 = 22 # Don't change
pin_lcd_contrast = 23 # Don't change
pin_lcd_enable = 25 # Don't change
pin_neoring = 2
pin_lcd_rs = 27 # Don't change
pin_lcd_db5 = 32 # Don't change
pin_lcd_db4 = 33 # Don't change
pin_buzzer = 26
pin_dht11 = 14
pin_neostrip_left = 4
pin_neostrip_right = 0
pin_mpu = None # connect via sda and scl
pin_ina = None # connect via sda and scl


##### CONFIGURATIONS
LCD_NUM_LINES = 4
LCD_NUM_COLUMNS = 20
GPS_BAUDRATE = 9600 # u-block default
GPS_PORT = 2 # Don't change


##### OBJECTS
gps=GPS_SIMPLE(UART(GPS_PORT,GPS_BAUDRATE)) # 5V
lcd=GpioLcd(rs_pin=Pin(pin_lcd_rs),
            enable_pin=Pin(pin_lcd_enable),
            d4_pin=Pin(pin_lcd_db4),
            d5_pin=Pin(pin_lcd_db5),
            d6_pin=Pin(pin_lcd_db6),
            d7_pin=Pin(pin_lcd_db7),
            num_lines=LCD_NUM_LINES,
            num_columns=LCD_NUM_COLUMNS) # 3.3V

solenoid = Pin(pin_solenoid,Pin.OUT)

ina=INA219(I2C(scl=Pin(pin_scl),sda=Pin(pin_sda),freq=400000)) # 3.3V

dht11=dht.DHT11(Pin(pin_dht11)) # 3.3V

buzzer_PWM_objekt=PWM(Pin(pin_buzzer,Pin.OUT),freq=1,duty=0) # 3.3V?

mpu=MPU6050(I2C(scl=Pin(pin_scl),sda=Pin(pin_sda),freq=400000)) # 3.3V

neoring=NeoPixel(Pin(pin_neoring,Pin.OUT),12) #Neopixel ring

lb=NeoPixel(Pin(pin_neostrip_left,Pin.OUT),3) #Venstre blinklys

rb=NeoPixel(Pin(pin_neostrip_right,Pin.OUT),3) #Højre blinklys

left_button=Pin(pin_button_left,Pin.IN)

right_button=Pin(pin_button_right,Pin.IN)


##### FUNCTIONS
def handler_alarm(req_id,method,params):
    """Handler callback to receive RPC from server, to enable or disable alarm"""
    print(f"Response: {req_id}: {method}, params {params}")
    print(params, "params type:", type(params))
    try:
        if method=="Enable alarm":
            if params==True:
                print("Alarm enabled")
                alarm_enabled=True
            elif params==False:
                print("Alarm disabled")
                alarm_enabled=False
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
    batt_percentage=((ina_voltage()-6)/(8.4-6.0))*100 # Return is %-based
    return batt_percentage

def batt_life():
    current=ina.get_current()
    return (3600*batt_percentage())/current

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

def color_long(r,g,b):
    """Turn off neopixel lights"""
    for i in range(12):
        neoring[i]=(r,g,b)
    neoring.write()

def color_short(np,r,g,b):
    for i in range(3):
        np[i]=(r,g,b)
    np.write()


def disable_active_alarm():
    """Disable sound and lights"""
    color_long(0,0,0)
    backend.color_short(rb,0,0,0)
    backend.color_short(rb,0,0,0)
    buzzer_PWM_objekt.duty(0)


def trigger_alarm(r,g,b,): #neoring, lb, rb
    """Trigger flashy lights and annoying sounds"""
    neopixel_flash(neoring,12,r,g,b)
    neopixel_flash(lb,3,r,g,b)
    neopixel_flash(rb,3,r,g,b)
    buzzer_PWM_objekt.freq(1023)
    buzzer_PWM_objekt.duty(512)
    # A delay - blocking or non-blocking??
    neopixel_flash(neoring,12,r,g,b)
    neopixel_flash(lb,3,r,g,b)
    neopixel_flash(rb,3,r,g,b)
    buzzer_PWM_objekt.freq(512)
    # A delay - blocking or non-blocking?


def blinker(n):
    """Function to make a signal light blink"""
    blinker_ticker=ticks_ms(neopixel)
    if ticks_ms()-blinker_ticker>100:
        for i in range(n):
            neopixel[i]=(0,50,50)
        neopixel.write()
        for i in range(n):
            neopixel[i]=(0,0,0)
        neopixel.write()
        blinker_ticker=ticks_ms()
