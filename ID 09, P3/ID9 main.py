"""
ID 9
Man skal kunne sende en besked til løsningen fra Thingsboard,
så den aktiverer eller deaktiverer et alarmsystem,
så den blinker kraftigt med lys og giver lyd fra sig,
hvis den rykker sig når alarmen er slået til.
"""

##### IMPORTS
from machine import Pin, PWM, I2C
from time import sleep, ticks_ms
from hardware_pins import pin_buzzer
from uthingsboard.client import TBDeviceMqttClient
from mpu6050 import MPU6050
from neopixel import NeoPixel
import gc
import secrets
from sys import exit 


##### PINS
buzzer=pin_buzzer
i2c = I2C(0) #I2C init. Pin 18 SCL, Pin 19 SDA
neopixel_ring=15


##### CONFIGURATIONS
n = 3 #Number of NeoPixels
alarm_triggered=False
alarm_enabled=False


##### OBJECTS
buzzer_PWM_objekt=PWM(Pin(buzzer,Pin.OUT),freq=1,duty=850)
imu = MPU6050(i2c) #MPU
np = NeoPixel(Pin(neopixel_ring, Pin.OUT), n) #np Object on Pin 16
client=TBDeviceMqttClient(secrets.SERVER_IP_ADDRESS,
                          access_token=secrets.ACCESS_TOKEN)


##### FUNCTIONS
def disable_active_alarm():
    neopixel_clear()
    buzzer_PWM_objekt.duty(0)

def neopixel_flash(r,g,b):
    for i in range(n):
        np[i]=(r,g,b)
    np.write()

def neopixel_clear():
    for i in range(n):
        np[i]=(0,0,0)
    np.write()

def trigger_alarm(r, g, b): #Farvefunktion til NeoPixels
    neopixel_flash(r,g,b)
    buzzer_PWM_objekt.freq(1023)
    buzzer_PWM_objekt.duty(512)
    sleep(0.5)
    neopixel_flash(b,g,r)
    buzzer_PWM_objekt.freq(512)
    buzzer_PWM_objekt.freq(512)
    sleep(0.5)

def hanlder(req_id, method, params):
    """Handler callback to receive RPC from server"""
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
    except TypeError as e:
        print(e)
        
client.connect()


##### PROGRAM
while True:
    if alarm_enabled==True:

        values = imu.get_values() #Henter værdier fra MPU
        if  values["acceleration x"] < -1000: # Tænd for alarm hvis 
            alarm_triggered=True
        if values["acceleration x"] > -1000: # Deaktiver lys og lyd
            alarm_triggered=False

        if alarm_triggered==False:
            disable_active_alarm()
        if alarm_triggered==True:
            trigger_alarm(255,0,0) #Funktion kaldes

    if alarm_enabled==False:
        alarm_triggered=False
        disable_active_alarm()