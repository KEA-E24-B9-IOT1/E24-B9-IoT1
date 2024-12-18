import secrets
import backend
import ID1_main
import ID2_main
import ID3_main
import ID4_main
import ID6_main
import ID7_main
import ID9_main
import ID11_main


from time import ticks_ms

##### Non blocking Delay Config #####

id1 = ticks_ms()
id2 = ticks_ms()
id3 = ticks_ms()
id4moving = ticks_ms()
id4alarm = ticks_ms()
id6 = ticks_ms()
id7 = ticks_ms()
id9 = ticks_ms()


##### Non Blocking Delay timing #####
#Opgives i ms
id1timing = 120000
id2timing = 5000
id3timing = 5000
id4movingtiming = 1000
id4alarmtiming= 180000
id6timing = 500
id7timing = 5000 # Skal være 300000
id9timing = 666 # SKAL ændres når ID9 bliver fikset


##### Startup configs
ID1_main.run()
# Make client object to connect to thingsboard
client = backend.TBDeviceMqttClient(secrets.SERVER_IP_ADDRESS, access_token = secrets.ACCESS_TOKEN)
client.connect() # Connecting to ThingsBoard
print("Connecting")
ID4AlarmSystem=False



##### Main Program
while True:
    try:            
        if ticks_ms() > id4moving + id4movingtiming:
            print("ID 4 is_moving running") # Cykel bevæget sig indenfor 3 min?
            id4moving = ticks_ms()
            ID4_main.is_moving()
            # SOMETHING?
        if ticks_ms() > id4alarm + id4alarmtiming:
            print("ID 4 alarm running") # Cykel stået stille i 3 min, aktiver alarm
            id4alarm = ticks_ms()
            ID4.main_alarm()
            # SOMETHING?
        if ID4AlarmSystem == True:
            values=ID6_main.mpu.get_values()
            if values["acceleration z"] > 2000 or values["acceleration y"] > 2000 or values["acceleration x"] > 2000:
                print("ID 4 alarm triggered, sending gps data to Thingsboard")
                id4telemetry=ID4_main.trigger_TB_alarm()
                client.send_telemetry(id4telemetry)
#         if ticks_ms() > id9 + id9timing:
#             print("ID 9 running")
#             id9 = ticks_ms()
    except KeyboardInterrupt:
        client.disconnect()               # Disconnecting from ThingsBoard
        reset()
