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

##### PINS
buzzer=pin_buzzer
i2c = I2C(0) #I2C init. Pin 18 SCL, Pin 19 SDA
neopixel_ring=15

##### CONFIGURATIONS
n = 12 #Number of NeoPixels
alarm_triggered=False

##### OBJECTS
buzzer_PWM_objekt=PWM(Pin(buzzer,Pin.OUT),freq=1,duty=850)
imu = MPU6050(i2c) #MPU
np = NeoPixel(Pin(neopixel_ring, Pin.OUT), n) #np Object on Pin 16

##### FUNCTIONS
def buzzer_alarm_loud(): # Buzzer alarm funktion
    buzzer_PWM_objekt.freq(1023)
    buzzer_PWM_objekt.duty(512)
def buzzer_alarm_quiet():
    buzzer_PWM_objekt.freq(512)
    buzzer_PWM_objekt.duty(512)
    
    
def trigger_alarm(r, g, b): #Farvefunktion til NeoPixels
    for i in range(n):
        np[i] = (r, g, b)
    np.write()
    buzzer_alarm_loud()
    sleep(0.5)
    for i in range(n):
        np[i]=(r,r,r)
    np.write()
    buzzer_alarm_quiet()
    sleep(0.5)


##### PROGRAM
while True:
    values = imu.get_values() #Henter værdier fra MPU
    if  values["acceleration x"] < -1000: # Tænder for bremselys, hvis over -1000
        alarm_triggered=True
    elif values["acceleration x"] > -1000:
        alarm_triggered=False
    if alarm_triggered==False:
        for i in range(n):
            np[i]=(0,0,0)
        np.write()
        buzzer_PWM_objekt.duty(0)
    if alarm_triggered==True:
        trigger_alarm(255,0,0) #Funktion kaldes
