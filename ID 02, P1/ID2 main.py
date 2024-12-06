##### IMPORTS
import gc

from time import sleep
from machine import reset
import hardware_pins_config as hw


##### OBJECTS
dht11=hw.dht11
lcd=hw.lcd


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
        if gps.receive_nmea_data() and gps.get_validity()=="A": # If gps data is received
            data={"La":gps.get_latitude(),
                  "Lo":gps.get_longitude(),
                  "Course":gps.get_course(),
                  "Speed":gps.get_speed(),
                  "Temp":dht11_temp(),
                  "Batt%":batt_percentage()}
            hw.display(f"Batt%:{data.get('Batt%'):.0f} Temp:{data.get('Temp')}")
            hw.display(f"La/Lo:{data.get('La'):.3f}/{data.get('Lo'):.3f}")
            hw.display(f"Lo:{data.get('Lo'):.2f}")
            # Lav Course om til at give kardinalværdier i stedet for tal
            hw.display(f"Speed:{data.get('Speed'):.1f} Course:{data.get('Course')}")
        sleep(1)                          # send telemetry once every second
    except KeyboardInterrupt:
        print("Disconnected!")
        reset()                           # reset ESP32
