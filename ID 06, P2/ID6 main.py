from mpu6050 import MPU6050
from time import ticks_ms
from machine import Pin, I2C
from neopixel import NeoPixel

n = 12 #Number of NeoPixels
np = NeoPixel(Pin(2, Pin.OUT), n) #np Object on Pin 16

i2c = I2C(0) #I2C init. Pin 18 SCL, Pin 19 SDA
imu = MPU6050(i2c) #MPU

def set_color(r, g, b): #Farvefunktion til NeoPixels
    for i in range(n):
        np[i] = (r, g, b)
    np.write()
    
def run:
    values = imu.get_values() #Henter værdier fra MPU
    if  values["acceleration y"] > 1000: # Tænder for bremselys, hvis over 1000
        set_color(255,0,0) #Funktion kaldes
        return 1000 #return mængden af tid bremselyset skal være tændt
    else:
        set_color(0,0,0)   #Funktion kaldes
        
