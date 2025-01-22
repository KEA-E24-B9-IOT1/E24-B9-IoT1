""" 
Denne fil er til ID 1.
Krav er som følgende:
Løsningen skal køre på batteri og skal som minimum kunne fungere i en time. 
Samtidig skal batteristatus, resterende kapacitet i procent, vises.
"""
import backend


# FUNCTIONS
def run():
    print("Display battery percentage")
    backend.display(0, 0, f"Bat%:{int(backend.batt_percentage())}")