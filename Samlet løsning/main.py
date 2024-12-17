import secrets
import backend
import ID1_main
import ID2_main
import ID3_main
import ID6_main


from time import ticks_ms

##### Non blocking Delay Config #####
id1 = ticks_ms()
id2 = ticks_ms()
id3 = ticks_ms()
id4 = ticks_ms()
id5 = ticks_ms()
id6 = ticks_ms()


##### Non Blocking Delay timing #####
#Opgives i ms
id1timing = 120000
id2timing = 5000
id3timing = 5000
# id4timing = None
# id5timing = None
id6timing = 500


##### Startups
ID1_main.run()
# Make client object to connect to thingsboard
client = backend.TBDeviceMqttClient(secrets.SERVER_IP_ADDRESS, access_token = secrets.ACCESS_TOKEN)
client.connect() # Connecting to ThingsBoard


##### Main Program
while True:
    try:
        if ticks_ms() > id1 + id1timing:
            id2 = ticks_ms()
            ID1_main.run()
        if ticks_ms() > id2 + id2timing:
            id2 = ticks_ms() # Resetter nonblocking delay timer
            ID2_main.run()
        if ticks_ms() > id3 + id3timing:
            id3 = ticks_ms()
            telemetry=ID3_main.run()
            client.send_telemetry(telemetry) #Sending telemetry  
    #     if ticks_ms() > id4 + id4timing:
#             id4 = ticks_ms()
    #         Pass
    #     if ticks_ms() > id5 + id5timing:
    #         id5 = ticks_ms()
#     Pass
        if ticks_ms() > id6 + id6timing:
            id6 = ticks_ms() + ID6_main.run() #Returnere positivt tal for at holde bremselyset tændt
    except KeyboardInterrupt:
        client.disconnect()               # Disconnecting from ThingsBoard
        reset()