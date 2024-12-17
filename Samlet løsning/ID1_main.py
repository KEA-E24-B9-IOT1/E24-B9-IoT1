""" 
Denne fil er til ID 1.
Krav er som følgende:
Løsningen skal køre på batteri og skal som minimum kunne fungere i en time. 
Samtidig skal batteristatus, resterende kapacitet i procent, vises.
"""
import backend as hw # Consistency

# CONFIGURATION


# OBJECTS
ina=hw.ina
# ina219.set_calibration_32V_2A() # Følsomhed, kan ændres


# FUNCTIONS
def batteri_percentage():
    voltage=ina219.get_bus_voltage()
    batt_percentage=((voltage-6)/(8.4-6))*100
    return batt_percentage

def procent():
    lcd.putstr(f"Batteriprocent: {batt_percentage()}")
    lcd.putstr(f"restlevetid: {3600/ina219.get_current()} timer")
    print(batt_percentage())
    sleep(0.5)
def levetid():
    
    
