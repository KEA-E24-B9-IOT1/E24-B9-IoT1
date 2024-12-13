from uthingsboard.client import TBDeviceMqttClient
from time import sleep
from machine import reset, UART, Pin
import gc
import secrets
from gps_simple import GPS_SIMPLE
import backend

gps_port = 2
gps_speed = 9600
uart = UART(gps_port, gps_speed)
gps = GPS_SIMPLE(uart)
dht11=backend.dht11

client = TBDeviceMqttClient(secrets.SERVER_IP_ADDRESS, access_token = secrets.ACCESS_TOKEN)
client.connect()

while True:
    try:
        dht11.measure()
        print(backend.dht11_temp())
        if gps.receive_nmea_data():
            if gps.get_validity()=="A":
                print(gps.receive_nmea_data())
                print(gps.get_longitude())
                print(gps.get_latitude())
                print(gps.get_course())
                print(gps.get_validity())
        telemetry = {"Temp":backend.dht11_temp()}
        client.send_telemetry(telemetry)
        sleep(1)
    except KeyboardInterrupt:
        print("Disconnected!")
        client.disconnect()
        reset()