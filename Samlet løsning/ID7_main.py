"""
Visning af den forventede resttid løsningen kan bruges.
Visningen skal være på lokal konsol, Educaboard, og på Thingsboard
"""

import backend


average_current=[] # List for the avg current consumption


def ina_current_average():
    """Fetch current consumption and calculate average consumption based on the last 36 measurements"""
    average_current.append(backend.ina_current()) # Append new measurement to the list
    if len(average_current)>36: # Check if the list of measurements is more than 36 items long
        del average_current[0] # Delete oldest measurement
    avg_current=sum(average_current)/len(average_current) # Calculate average based on sum and length of list
    print(f"Avg current: {avg_current}") # For troubleshooting
    return avg_current # Return average current consumption

def est_batt_life():
    battlife=3600*(backend.batt_percentage()/100)/ina_current_average() # Calculate estimated remaining battery hours based on average consumption and current batt &
    telemetry = {'Battlife' : battlife} # Save battlife
    print(f"Est. batt life: {battlife}") # For troubleshooting
    backend.display(0, 0, "         ") # Clear screen from previous batt% or batt life
    backend.display(0, 0, f"Bat:{int(battlife)}T") # Display calculated batt life
    return telemetry # Return batt life to be uploaded to thingsboard
    
