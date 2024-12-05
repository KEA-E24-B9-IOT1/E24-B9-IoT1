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
from sys import exit


##### VARIABLES AND CONSTANTS
gps_loc=None
gps_ticker=ticks_ms()
gps_three_min_ticker=ticks_ms()
gps_alarm_ticker=ticks_ms()
gps_list=[]
AlarmSystemEnabled=False
gps_alarm_ticker=ticks_ms()
gps_alarm_thingsboard_ticker=ticks_ms()


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


##### FUNCTIONS
def handler(req_id, method, params):
    """Handler callback to receive RPC from server"""
    print(f"Response: {req_id}: {method}, params {params}")
    print(params, "params type:", type(params))
    try:
        if method=="Disable alarm":
            if params==True:
                print("Alarm enabled")
            else:
                print("Alarm disabled")
                exit()
        if method=="sendCommand":
            print(params.get("command"))
    except TypeError as e:
        print(e)

client.connect()


##### PROGRAM
while True:
    try:
        if gc.mem_free() < 2000:          # free memory if below 2000 bytes left
            gc.collect()
        if gps.receive_nmea_data() and gps_loc==None:
            gps_loc={"Latitude":gps.get_latitude(),
                     "Longitude":gps.get_longitude()}
            print("Initial gps coordinates collected")
        if ticks_ms()-gps_ticker>20000:
            gps_update={"Latitude":gps.get_latitude(),
                        "Longitude":gps.get_longitude()}
            gps_list.append(gps_update)
            if len(gps_list)>19:
                del gps_list[0]
            gps_ticker=ticks_ms()
        if ticks_ms()-gps_three_min_ticker>10000: #180000
            gps_three_min_ticker=ticks_ms()
            if any(dictionary['Latitude']==gps.get_latitude() for dictionary in gps_list):
                print("Enabling alarm system")
                AlarmSystemEnabled=True
                gps_alarm_loc={"Latitude":gps.get_latitude(),
                               "Longitude":gps.get_longitude()}            
        if AlarmSystemEnabled:
            if gps.get_latitude() and gps.get_longitude() not in gps_list:
                print("Motion detected! Sending coordinates to thingsboard")
                if ticks_ms()-gps_alarm_thingsboard_ticker>10000:
                    telemetry={"Latitude":gps.get_latitude,"Longitude":gps.get_longitude()}
                    client.send_telemetry(telemetry)
                    gps_alarm_thingsboard_ticker=ticks_ms()
        client.set_server_side_rpc_request_handler(handler)
        client.check_msg()
    except KeyboardInterrupt:
        print("Disconnected!")
        reset()                           # reset ESP32