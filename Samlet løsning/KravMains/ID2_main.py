##### IMPORTS
import gc

from time import sleep
from machine import reset
import backend as hw #Omdøbt


##### OBJECTS
dht11=hw.dht11
lcd=hw.lcd

# Variabels
global counter
counter = 0
##### PROGRAM
def run():    
    print(f"free memory: {gc.mem_free()}") # monitor memory left
    if gc.mem_free() < 2000:          # free memory if below 2000 bytes left
        print("Garbage collected!")
        gc.collect()                  # free memory
# Raffiner hvilken data vi henter og gemmer hvornår
    if hw.gps.receive_nmea_data() and hw.gps.get_validity()=="A": # If gps data is received
        la = hw.gps.get_latitude()
        lo = hw.gps.get_longitude()
        course = hw.gps.get_course()
        speed = hw.gps.get_speed()
    else:
        la = "la"
        lo = "lo"
        course = "cou"
        speed = "spe"
    data={"La":la,
          "Lo":lo,
          "Course":course,
          "Speed":speed,
          "Temp":hw.dht11_temp(),
          "Batt%":hw.batt_percentage()
          }
    hw.display(0,  0, f"Bat%:{data.get('Batt%'):.0f}")
    hw.display(10, 0, f"Temp:{data.get('Temp')}")
    hw.display(0,  1, f"La/Lo:{float(data.get('La')):.3f}/{float(data.get('Lo')):.3f}")
    # hw.display(0, 2, f"Lo:{data.get('Lo'):.2f}")
    # Lav Course om til at give kardinalværdier i stedet for tal
    hw.display(0, 2,  f"Speed:{data.get('Speed'):.1f} Course:{data.get('Course')}")
    global counter
    hw.display(10, 3, str(counter))
    counter += 1


