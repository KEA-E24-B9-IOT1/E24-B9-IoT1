import secrets
import backend
import ID1_main
import ID2_main
import ID3_main
import ID6_main
import ID7_main


from time import ticks_ms

##### Non blocking Delay Config #####

id1 = ticks_ms()
id2 = ticks_ms()
id3 = ticks_ms()
id4 = ticks_ms()
id5 = ticks_ms()
id6 = ticks_ms()
id7 = ticks_ms()

##### Non Blocking Delay timing #####
#Opgives i ms
ina_meas = 1000
id1timing = 120000
id2timing = 5000
id3timing = 5000
# id4timing = None
# id5timing = None
id6timing = 500
id7timing = 5000 # Skal være 300000


##### Startups
ID1_main.run()
# Make client object to connect to thingsboard
client = backend.TBDeviceMqttClient(secrets.SERVER_IP_ADDRESS, access_token = secrets.ACCESS_TOKEN)
client.connect() # Connecting to ThingsBoard



##### Main Program
while True:
    try:
        if ticks_ms() > id1 + id1timing:
            id1 = ticks_ms()
            ID1_main.run()
        if ticks_ms() > id2 + id2timing:
            id2 = ticks_ms() # Resetter nonblocking delay timer
            ID2_main.run()
        if ticks_ms() > id3 + id3timing:
            id3 = ticks_ms()
            id3telemetry=ID3_main.run()
            client.send_telemetry(id3telemetry) #Sending telemetry
#         if ticks_ms() > id4 + id4timing:
#             id4 = ticks_ms()
#             ID4_main.run(ticks_ms())
    #     if ticks_ms() > id5 + id5timing:
    #         id5 = ticks_ms()
#     Pass
        if ticks_ms() > id6 + id6timing:
            id6 = ticks_ms() + ID6_main.run() #Returnere positivt tal for at holde bremselyset tændt
        if ticks_ms() > id7 + id7timing:
            id7 = ticks_ms()
            id7telemetry=ID7_main.run()
            client.send_telemetry(id7telemetry)
    except KeyboardInterrupt:
        client.disconnect()               # Disconnecting from ThingsBoard
        reset()