##### IMPORTS
import gc

from time import sleep
from machine import reset
import backend


##### PROGRAM
def run():    
    print(f"free memory: {gc.mem_free()}") # monitor memory left
    if gc.mem_free() < 2000:          # free memory if below 2000 bytes left
        print("Garbage collected!")
        gc.collect()                  # free memory
# Raffiner hvilken data vi henter og gemmer hvornår
    if backend.gps.receive_nmea_data():
        print("Display temp")
        backend.display(10, 0, f"Temp:{backend.dht11_temp():.1f}")
        if backend.gps.get_validity()=="A": # If gps data is received
            print("Display gps data")
            backend.display(0,  1, f"La/Lo:{backend.gps.get_latitude():.3f}/{backend.gps.get_longitude():.3f}")
            # Lav Course om til at give kardinalværdier i stedet for tal
            backend.display(0, 2, f"Speed:{backend.gps.get_speed():.1f}")
            backend.display(0, 3, f"Course:{backend.gps.get_course()}")
        if backend.gps.get_validity()=="V":
            print("Display gps unavailable")
            backend.display(0,  1, f"GPS unavailable")