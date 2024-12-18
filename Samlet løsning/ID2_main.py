"""
På den lokale konsol, Educaboard, skal vises hastighed, retning, længde- og breddegrad, batteristatus og temperatur
"""

##### IMPORTS
import gc
import backend

##### PROGRAM
def run():
    """Fetch and show GPS data"""
    backend.gps.receive_nmea_data()
    print(f"free memory: {gc.mem_free()}") # monitor memory left
    if gc.mem_free() < 2000: # free memory if below 2000 bytes left
        print("Garbage collected!")
        gc.collect() # free memory
    if backend.gps.receive_nmea_data(): # If gps data is available
        print("Display temp") # For troubleshooting
        backend.display(10, 0, f"Temp:{backend.dht11_temp():.1f}") # Display temp with 1 decimal
        if backend.gps.get_validity()=="A": # If gps data is validated
            print("Display gps data") # For troubleshooting
            backend.display(0,  1, f"La/Lo:{backend.gps.get_latitude():.3f}/{backend.gps.get_longitude():.3f}") # Show lat/lon on LCD with 3 decimals
            # 3 decimals is an accuracy down to 111m according to Garmin
            backend.display(0, 2, f"Speed:{backend.gps.get_speed():.1f}") # Display speed from gps
            backend.display(0, 3, f"Course:{backend.gps.get_course()}") # Display which course the gps is moving
        if backend.gps.get_validity()=="V": # If gps data is inavlid
            print("Display gps unavailable")
            backend.display(0,  1, f"GPS unavailable") # Display that gps data ins invalid
