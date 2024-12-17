##### IMPORTS
import gc

from time import sleep
from machine import reset
import backend as hw #Omdøbt

# Variabels
printable=None

##### PROGRAM
def run():    
    print(f"free memory: {gc.mem_free()}") # monitor memory left
    if gc.mem_free() < 2000:          # free memory if below 2000 bytes left
        print("Garbage collected!")
        gc.collect()                  # free memory
# Raffiner hvilken data vi henter og gemmer hvornår
    if hw.gps.receive_nmea_data():
        hw.display(10, 0, f"Temp:{hw.dht11_temp():.1f}")
        if hw.gps.get_validity()=="A": # If gps data is received
            la = hw.gps.get_latitude()
            lo = hw.gps.get_longitude()
            course = hw.gps.get_course()
            speed = hw.gps.get_speed()
            printable=True
        if hw.gps.get_validity()=="V":
            printable=False
        if printable==True:
            hw.display(0,  1, f"La/Lo:{hw.gps.get_latitude():.3f}/{hw.gps.get_longitude():.3f}")
            # Lav Course om til at give kardinalværdier i stedet for tal
            hw.display(0, 2, f"Speed:{data.get('Speed'):.1f}")
            hw.display(0, 3, f"Course:{data.get('Course')}")
        if printable==False:
            hw.display(0,  1, f"GPS unavailable")
