import secrets
import backend
import ID1_main
import ID2_main
import ID3_main
import ID6_main
import ID7_main
# import ID9_main
import ID11_main


from time import ticks_ms

##### Non blocking Delay Config #####

id1 = ticks_ms()
id2 = ticks_ms()
id3 = ticks_ms()
id4 = ticks_ms()
id6 = ticks_ms()
id7 = ticks_ms()
id9 = ticks_ms()
id11 = ticks_ms()


##### Non Blocking Delay timing #####
#Opgives i ms
id1timing = 120000
id2timing = 5000
id3timing = 5000
id4timing = 666 # SKAL ændres når ID4 bliver fikset
id6timing = 500
id7timing = 5000 # Skal være 300000
id9timing = 666 # SKAL ændres når ID9 bliver fikset
id11timing = 100 # Hvor længe inden pb-værdi tjekkes igen


##### Startup configs
# right_blinker_toggle=False
# left_blinker_toggle=False
ID1_main.run()
# Make client object to connect to thingsboard
client = backend.TBDeviceMqttClient(secrets.SERVER_IP_ADDRESS, access_token = secrets.ACCESS_TOKEN)
client.connect() # Connecting to ThingsBoard
print("Connecting")



##### Main Program
while True:
    try:            
        if ticks_ms() > id1 + id1timing:
            print("ID 1 running")
            id1 = ticks_ms()
            ID1_main.run()
        if ticks_ms() > id2 + id2timing:
            print("ID 2 running")
            id2 = ticks_ms() # Resetter nonblocking delay timer
            ID2_main.run()
        if ticks_ms() > id3 + id3timing:
            print("ID 3 running")
            id3 = ticks_ms()
            id3telemetry=ID3_main.run()
            client.send_telemetry(id3telemetry) #Sending telemetry
#         if ticks_ms() > id4 + id4timing:
#             print("ID 4 running")
#             id4 = ticks_ms()
#             ID4_main.run(ticks_ms())
        if ticks_ms() > id6 + id6timing:
            print("ID 6 running")
            id6 = ticks_ms() + ID6_main.run() #Returnere positivt tal for at holde bremselyset tændt
        if ticks_ms() > id7 + id7timing:
            print("ID 7 running")
            id7 = ticks_ms()
            id7telemetry=ID7_main.est_batt_life()
            client.send_telemetry(id7telemetry)
        if ticks_ms() > id9 + id9timing:
            print("ID 9 running")
            id9 = ticks_ms()
        if ID11_main.left_button.value()==1:
            print("ID 11 left running")
            ID11_main.left_blinker_func()
        if ID11_main.right_button.value()==1:
            print("ID 11 right running")
            ID11_main.right_blinker_func()
    except KeyboardInterrupt:
        client.disconnect()               # Disconnecting from ThingsBoard
        reset()