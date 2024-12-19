"""
Når cyklen har stået stille i mere end 3 minutter, og brugeren ikke har slukket permanent for løsningen, sendes beskeder med cyklens placering til Thingsboard, hvis cyklen kommer i bevægelse
"""

##### IMPORTS
import gc
import backend


##### VARIABLES AND CONSTANTS
gps_loc=[] # For saving locations
gps_loc_list=[] # For saving locations


##### Functions
def is_moving():
    """See if the bike is moving"""
    backend.gps.receive_nmea_data() # Fetch gps data
    if gc.mem_free() < 2000: # Clear memory if less than 2000
        gc.collect() # Clear memory
    if backend.gps.receive_nmea_data() and backend.gps.get_validity()=="A": # Check if there's data and if it's valid
        print("Bike gps") # For troubleshooting
        gps_loc={"Latitude":backend.gps.get_latitude(),
                 "Longitude":backend.gps.get_longitude()} # Save data
        gps_loc_list.append(gps_loc) # Append to a list
        if len(gps_loc_list)>180: # Keep a max of 180 items in the list
            del gps_loc_list[0] # Delete oldest entry


def alarm():
    """Check if the bike has been stationary, in which case the alarm should be enabled"""
    print("Alarmsystem check") # For troubleshooting
    if gc.mem_free() < 2000: # Clear memory if less than 2000
        gc.collect() # Clear memory
    if any(dictvalue1['Latitude']==backend.gps.get_latitude() for dictvalue1 in gps_loc_list) and any(dictvalue2['Longitude']==backend.gps.get_longitude() for dictvalue2 in gps_loc_list): # See if current gps location is in the list of 180 entries, in which case the alarm should be enabled
            print("Enabling alarm system") # For troubleshooting
            return True # Return bool to main.py for the trigger_TB_alarm function


def trigger_TB_alarm():
    """If alarm is enabled and the bike is moved, send data to Thingsboard"""
    print("TB alarm triggered") # For troubleshooting
    telemetry={"Latitude":backend.gps.get_latitude(),"Longitude":backend.gps.get_longitude()} # Save gps data
    return telemetry # Return gps data for upload in main.py
