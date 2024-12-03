"""
Krav: 
Når cyklen har stået stille i mere end 3 minutter, 
og brugeren ikke har slukket permanent for løsningen, 
sendes beskeder med cyklens placering til Thingsboard, 
hvis cyklen kommer i bevægelse

Accepttest: 
- Batteri skal være fuldt opladet 
- Løsningen tændes 
- En kort tur på 1 minut køres 
- Cyklen stilles, men løsningen slukkes ikke, og tiden nulstilles 
- Når der ikke er registreret bevægelse på cyklen i 3 minutter fra 3) 
skal der inden for 30 sekunder komme en besked på Thingsboard hvis cyklen kommer i bevægelse, 
og positionen sendes hvert tiende sekund til Thingsboard. Sker dette er kravet opfyldt.
"""

##### IMPORTS
from uthingsboard.client import TBDeviceMqttClient
from time import ticks_ms, sleep
from machine import reset, UART, Pin
import gc
from gps_simple import GPS_SIMPLE
import secrets


##### PINS
# ESP32 UART port, Educaboard ESP32 default UART port
gps_port = 2

##### CONFIGURATIONS
# UART speed, defauls u-blox speed
gps_speed = 9600


##### OBJECTS
uart = UART(gps_port, gps_speed)
gps = GPS_SIMPLE(uart)
client=TBDeviceMqttClient(secrets.SERVER_IP_ADDRESS,access_token=secrets.ACCESS_TOKEN)
gps_ticker=ticks_ms()

##### FUNCTIONS
client.connect()


##### PROGRAM
while True:
    try:
        if gc.mem_free() < 2000:          # free memory if below 2000 bytes left
            print("Garbage collected!")
            gc.collect()                  # free memory 
        if gps.receive_nmea_data():
            gps_loc={"Latitude":gps.get_latitude(),
                     "Longitude":gps.get_longitude()}
            if ticks_ms()-gps_ticker>5000:
                gps_update={"Latitude":gps.get_latitude(),
                            "Longitude":gps.get_longitude()}
                gps_ticker=ticks_ms()
                print(f"start lat = {gps_loc.get('Latitude')}")
                print(f"updated lat = {gps_update.get('Latitude')}")
                print(f"diff = {gps_loc.get('Latitude') - gps_update.get('Latitude')}")
                print(f"start lon = {gps_loc.get('Longitude')}")
                print(f"updated lon = {gps_update.get('Longitude')}")
                print(f"diff = {gps_loc.get('Longitude') - gps_update.get('Longitude')}")
        sleep(1)                          # send telemetry once every second
    except KeyboardInterrupt:
        print("Disconnected!")
        reset()                           # reset ESP32