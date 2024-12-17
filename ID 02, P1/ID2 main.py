##### IMPORTS
import gc

from time import sleep
from machine import reset
import backend as hw


##### OBJECTS
dht11=hw.dht11
lcd=hw.lcd
gps=hw.gps


##### PROGRAM
while True:
    try:
        print(f"free memory: {gc.mem_free()}") # monitor memory left
        if gc.mem_free() < 2000:          # free memory if below 2000 bytes left
            print("Garbage collected!")
            gc.collect()                  # free memory
            """
Raffiner hvilken data vi henter og gemmer hvornår
"""
        if gps.receive_nmea_data(): # If gps data is received
            if gps.get_validity()=="A":
                data={"La":gps.get_latitude(),
                      "Lo":gps.get_longitude(),
                      "Course":gps.get_course(),
                      "Speed":gps.get_speed(),
                      "Temp":hw.dht11_temp(),
                      "Batt%":hw.batt_percentage()}
                hw.display(0,0,f"Batt%:{data.get('Batt%'):.0f} Temp:{data.get('Temp')}")
                hw.display(0,1,f"La/Lo:{data.get('La'):.3f}/{data.get('Lo'):.3f}")
                hw.display(0,2,f"Speed:{data.get('Lo'):.2f}")
                # Lav Course om til at give kardinalværdier i stedet for tal
                hw.display(0,3,f"Course:{data.get('Course')}")
            if gps.get_validity()=="V":
                data={"La":gps.get_latitude(),
                      "Lo":gps.get_longitude(),
                      "Course":gps.get_course(),
                      "Speed":gps.get_speed(),
                      "Temp":hw.dht11_temp(),
                      "Batt%":hw.batt_percentage()}
                hw.display(0,0,f"Batt%:{data.get('Batt%'):.0f} Temp:{data.get('Temp')}")
                hw.display(0,1,f"La/Lo:N/A")
                hw.display(0,2,f"Speed:N/A")
                # Lav Course om til at give kardinalværdier i stedet for tal
                hw.display(0,3,f"Course:N/A")
        sleep(1)                          # send telemetry once every second
    except KeyboardInterrupt:
        print("Disconnected!")
        reset()                           # reset ESP32
