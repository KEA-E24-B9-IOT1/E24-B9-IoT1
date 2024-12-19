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
"""A colleciton of timers for various functions"""
id1 = ticks_ms()
id2 = ticks_ms()
id3 = ticks_ms()
id4moving = ticks_ms()
id4alarm = ticks_ms()
id6 = ticks_ms()
id7 = ticks_ms()


##### Non Blocking Delay timing #####
# In milliseconds
id1timing = 180000 # How often to execute ID 1
id2timing = 5000 # How often to execute ID 2
id3timing = 5000 # How often to execute ID 3
id4movingtiming = 1000 # How often to check ID 4 if the bike is moving
id4alarmtiming= 180000 # How often to check ID 4 for alarm arming, if not armed
id6timing = 500 # How often to check if ID 6 should be executed
id7timing = 300000 # How often to execute ID 7 for estimated battery life


##### Startup configs
ID1_main.run() # Startup battery life to display
# Make client object to connect to thingsboard
client = backend.TBDeviceMqttClient(secrets.SERVER_IP_ADDRESS, access_token = secrets.ACCESS_TOKEN)
client.connect() # Connecting to ThingsBoard
print("Connecting") # For troubleshooting
ID4AlarmSystem = False # For ID 4 alarm system
ID9AlarmSystem = False # For ID 9 alarm system
Solenoid_Toggle = False # Solenoid active/inactive state


##### Functions
def alarm_handler(req_id, method, params):
    """Handler callback to receive RPC from server"""
    print(f"Response: {req_id}: {method}, params {params}")
    print(params, "params type:", type(params))
    try:
        global ID9AlarmSystem
        if method == "Enable alarm":
            if params == True:
                print("Alarm enabled")
                ID9AlarmSystem = True
            elif params == False:
                print("Alarm disabled")
                ID9AlarmSystem = False
    except TypeError as e:
        print(e)

def solenoid_handler(req_id, method, params):
    """Handler callback to receive RPC from server"""
    print(f"Response: {req_id}: {method}, params {params}")
    print(params, "params type:", type(params))
    try:
#         global Solenoid_Toggle
        if method == "Solenoid state":
            if params == True:
                print("Solenoid enabled")
#                 Solenoid_Toggle = True
                backend.solenoid.value(1)
            elif params == False:
                print("Solenoid disabled")
#                 Solenoid_Toggle = False
                backend.solenoid.value(0)
    except TypeError as e:
        print(e)


client.set_server_side_rpc_request_handler(alarm_handler) # Thingsboard-Alarm connection
client.set_server_side_rpc_request_handler(solenoid_handler) # Thingsboard-Solenoid connection


##### Main Program
while True:
    try:
        client.check_msg() # As above
        if ticks_ms() > id1 + id1timing: 
            print("ID 1 running") # For troubleshooting
            id1 = ticks_ms() # Reset non-blocking delay
            ID1_main.run() # Execute ID 1. See ID1_main.py for more info.
        if ticks_ms() > id2 + id2timing:
            print("ID 2 running") # Display temp & GPS
            id2 = ticks_ms() # Resetter nonblocking delay timer
            ID2_main.run() # Execute ID2. See ID2_main.py for more info.
        if ticks_ms() > id3 + id3timing:
            print("ID 3 running")
            id3 = ticks_ms()
            id3telemetry=ID3_main.run() # Execute ID3 and save info for upload to Thingsboard. See ID3_main.py for more info.
            client.send_telemetry(id3telemetry) #Sending telemetry to Thingsboard
        if ticks_ms() > id4moving + id4movingtiming:
            if ID4AlarmSystem==False: # Only run following indentation if alarm isn't armed'
                print("ID 4 is_moving running") # For troubleshooting
                id4moving = ticks_ms()
                ID4_main.is_moving()
        if ticks_ms() > id4alarm + id4alarmtiming:
            if ID4AlarmSystem==True: # Only run following indentation if alarm isn't armed
                print("ID 4 alarm running") # Cykel stået stille i 3 min, aktiver alarm
                id4alarm = ticks_ms()
                ID4AlarmSystem=ID4_main.alarm()
        if ID4AlarmSystem == True: # Only run following indentation if alarm is armed
            values=ID6_main.mpu.get_values() # Fetch values
            if values["acceleration y"] > 5000 or values["acceleration x"] > 5000: # Execute following indentation if bike is moved horizontally
                print("ID 4 alarm triggered, sending gps data to Thingsboard") # For troubleshooting
                id4telemetry=ID4_main.trigger_TB_alarm() # Execute specified function from ID4 and save data.
                client.send_telemetry(id4telemetry) # Send saved data to Thingsboard.
                ID4AlarmSystem=False # Disable alarm as it's been triggered.
        if ticks_ms() > id6 + id6timing:
            print("ID 6 running")
            id6 = ticks_ms() + ID6_main.run() # Return positive number to extend brake light function.
        if ticks_ms() > id7 + id7timing:
            print("ID 7 running")
            id7 = ticks_ms()
            id7telemetry=ID7_main.est_batt_life() # Execute ID 7 and save estimated battery life.
            client.send_telemetry(id7telemetry) # Upload data to thingsboard.
        if ID9AlarmSystem == True: # Only run following indentation if ID9 alarm system is enabled
            values=ID6_main.mpu.get_values()
            if values["acceleration y"] < -1000 or values["acceleration y"] > 10000 or values["acceleration x"] < -1000 or values["acceleration x"] > 10000: # Trigger if the MPU registers movement
                print("Trigger id 9 alarm") # For troubleshooting
                ID9_main.id_9_alarm(True) # Run alarm section of ID9_main.py
            else:
                ID9_main.id_9_alarm(False) # For turning off light and sound from alarm
        if backend.left_button.value()==1 or backend.right_button.value()==1: # See if buttons have changed value, for the blinker
            if backend.left_button.value()==1: # Check if left button is manipulated
                print("ID 11 left running") # Troubleshooting
                backend.left_blinker_func() # Execute function for left signal blinker
            if backend.right_button.value()==1: # Check if right button
                print("ID 11 right running") # -||-
                backend.right_blinker_func() # -||-
    except KeyboardInterrupt:
        client.disconnect() # Disconnecting from ThingsBoard
        reset() # Reset ESP
