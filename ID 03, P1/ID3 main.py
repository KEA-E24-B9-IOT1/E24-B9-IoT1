# -*- coding: utf-8 -*-
#
# Copyright 2024 Kevin Lindemark
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

from uthingsboard.client import TBDeviceMqttClient
from time import sleep
from machine import reset, UART
import gc
import secrets
from gps_simple import GPS_SIMPLE
import dht
from adc_sub import ADC_substitute

dht11_pin=19
adc_pin=34
gps_port = 2                               # ESP32 UART port, Educaboard ESP32 default UART port
gps_speed = 9600                           # UART speed, defauls u-blox speed
uart = UART(gps_port, gps_speed)           # UART object creation
gps = GPS_SIMPLE(uart)                     # GPS object creation  
adc=ADC_substitute(adc_pin)
dht11=dht.DHT11(Pin(dht11_pin))

def get_lat_lon():
    lat = lon = None                       # create lat and lon variable with None as default value
    if gps.receive_nmea_data():            # check if data is recieved
                                           # check if the data is valid
        if gps.get_latitude() != -999.0 and gps.get_longitude() != -999.0 and gps.get_validity() == "A":
            lat = str(gps.get_latitude())  # store latitude in lat variable
            lon = str(gps.get_longitude()) # stor longitude in lon variable
            return lat, lon                # multiple return values, needs unpacking or it will be tuple format
        else:                              # if latitude and longitude are invalid
            print(f"GPS data to server not valid:\nlatitude: {lat}\nlongtitude: {lon}")
            return False
    else:
        return False
    
def dht11_temp():
    dht11.measure()
    tempC=dht11.temperature()
    return tempC

def batt_percentage():
    voltage=adc.read_voltage()*2
    batt_percentage=((voltage-3)/(4.2-3.0))*100
    return batt_percentage
                                           # Make client object to connect to thingsboard
client = TBDeviceMqttClient(secrets.SERVER_IP_ADDRESS, access_token = secrets.ACCESS_TOKEN)
client.connect()                           # Connecting to ThingsBoard
print("connected to thingsboard, starting to send and receive data")
while True:
    try:
        print(f"free memory: {gc.mem_free()}") # monitor memory left
        
        if gc.mem_free() < 2000:          # free memory if below 2000 bytes left
            print("Garbage collected!")
            gc.collect()                  # free memory 
        
        lat_lon = get_lat_lon()           # multiple returns in tuple format
        print(lat_lon)
        if lat_lon:
                                          # store telemetry in dictionary      
            telemetry = {'Latitude': lat_lon[0],
                         'Longitude': lat_lon[1],
                         'Course' : gps.get_course(),
                         'Speed' : gps.get_speed(),
                         'Temperature' : dht11_temp(),
                         'Batteri Percentage' : batt_percentage()}
            client.send_telemetry(telemetry) #Sending telemetry  
        sleep(1)                          # send telemetry once every second
    except KeyboardInterrupt:
        print("Disconnected!")
        client.disconnect()               # Disconnecting from ThingsBoard
        reset()                           # reset ESP32