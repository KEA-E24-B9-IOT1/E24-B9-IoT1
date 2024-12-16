##### IMPORTS
import gc

from time import sleep
from machine import reset
import backend as hw #Omdøbt


##### OBJECTS
dht11=hw.dht11
lcd=hw.lcd


##### PROGRAM
def run():
    try:
        print(f"free memory: {gc.mem_free()}") # monitor memory left
        if gc.mem_free() < 2000:          # free memory if below 2000 bytes left
            print("Garbage collected!")
            gc.collect()                  # free memory

# Raffiner hvilken data vi henter og gemmer hvornår

        if hw.gps.receive_nmea_data() and hw.gps.get_validity()=="A": # If gps data is received
            data={"La":hw.gps.get_latitude(),
                  "Lo":hw.gps.get_longitude(),
                  "Course":hw.gps.get_course(),
                  "Speed":hw.gps.get_speed(),
                  "Temp":None,#hw.dht11_temp(),
                  "Batt%":hw.batt_percentage()}
            hw.display(0,  0, f"Batt%:{data.get('Batt%'):.0f}")
            hw.display(10, 0, f"Temp:{data.get('Temp')}")
            hw.display(0,  1, f"La/Lo:{data.get('La'):.3f}/{data.get('Lo'):.3f}")
            hw.display(10, 1, f"Lo:{data.get('Lo'):.2f}")
            # Lav Course om til at give kardinalværdier i stedet for tal
            hw.display(0, 2,  f"Speed:{data.get('Speed'):.1f} Course:{data.get('Course')}")
            print(data)                         
    except KeyboardInterrupt:
        print("Disconnected!")
        reset()                           # reset ESP32

