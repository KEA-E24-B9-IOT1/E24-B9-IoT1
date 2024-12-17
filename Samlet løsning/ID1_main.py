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
def run():
    hw.display(0,  0, f"Bat%:{int(hw.batt_percentage())}")
    
    
