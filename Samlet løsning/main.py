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
id8 = ticks_ms()
id9 = ticks_ms()
id11 = ticks_ms()


##### Non Blocking Delay timing #####
#Opgives i ms
ina_meas = 1000
id1timing = 120000
id2timing = 5000
id3timing = 5000
id4timing = 666 # SKAL ændres når ID4 bliver fikset
id6timing = 500
id7timing = 5000 # Skal være 300000
id9timing = 666 # SKAL ændres når ID9 bliver fikset
id11timing = 100 # Hvor længe inden pb-værdi tjekkes igen


##### Startup configs
right_blinker_toggle=False
left_blinker_toggle=False
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
        if ticks_ms() > id4 + id4timing:
            id4 = ticks_ms()
#             ID4_main.run(ticks_ms())
        if ticks_ms() > id6 + id6timing:
            id6 = ticks_ms() + ID6_main.run() #Returnere positivt tal for at holde bremselyset tændt
        if ticks_ms() > id7 + id7timing:
            id7 = ticks_ms()
            id7telemetry=ID7_main.est_batt_life()
            client.send_telemetry(id7telemetry)
        if ticks_ms() > id9 + id9timing:
            id9 = ticks_ms()
       if ticks_ms() > id11 + id11timing:
            id11 = ticks_ms()
            ID11_main.run(left_counter,right_counter)
        
        pb_first_left = backend.left_button.value()
        pb_first_right = backend.right_button.value()
        if ticks_ms() > id11 + id11timing:
            pb_second_left = backend.left_button.value()
            pb_second_right = backend.right_button.value()
            if pb_first_left==1 and pb_second_left==0:
#                 global left_counter
#                 left_counter = 6
#                 
#                 left_blinker_toggle = not left_blinker_toggle
#                 if left_blinker_toggle == False:
#                     ID11_main.left_blinker.off()
#                 if left_blinker_toggle== True:
#                     ID11_main.left_blinker_func(ticks_ms())
#             if pb_first_right==1 and pb_second_right==0:
#                 right_blinker_toggle = not right_blinker_toggle
#                 if right_blinker_toggle == False:
#                     ID11_main.right_blinker.off()
#                 if right_blinker_toggle== True:
#                     ID11_main.right_blinker_func()
    except KeyboardInterrupt:
        client.disconnect()               # Disconnecting from ThingsBoard
        reset()