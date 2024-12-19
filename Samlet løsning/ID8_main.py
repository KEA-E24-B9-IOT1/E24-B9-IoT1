# Skal hede main.py på ladeløsningen's ESP32
# boot.py skal indeholde functionalitet til at logge på WiFi
# secrets.py skal indeholde 2 variabler: "SSID" og "PASSWORD" som indeholder SSID og Password til WiFi

import requests
from time import ticks_ms
from machine import Pin

#Nonblocking delay config
threshold_update = 15*60*1000 # 15 min til millisekunder
starttime_update = ticks_ms() - threshold_update # Så starter functionen med at hente data, fremfor at vente

#Pin Config
relay = Pin(15, Pin.OUT)
blue = Pin(32, Pin.OUT)
#Opstart
relay.value(0)   # Slukker for relæ
blue.value(1)    # Tænder for blåt lys, og indikere at der ikke er forbindelse eller grøn strøm
'''
# Simulering af skiftene grøn strøm
sim = 55
def simulering():
    global sim
    if sim == 55:
        sim = 45
    else:
        sim = 55
    return sim
'''
def fetch_green_power(): # Funktion der henter information fra API
    response = requests.get(
        url = "https://api.energidataservice.dk/dataset/CO2Emis?limit=2")
    co2emis = response.json().get('records')[1].get('CO2Emission') # Henter information fra json dict.
    print(f'gram CO2 / kWh : {co2emis}')
    if co2emis == None:
        return 0
    #co2emis = simulering()
    return co2emis

def led_green_power(): # Funktion der tænder når der er grøn strøm
    relay.value(1) # Tænder for relæ, så opladning startes
    blue.value(0)  # Slukker for blåt lys
def led_no_green_power(): # Funktion der tænder når der IKKE er grøn strøm
    relay.value(0) # Slukker for relæ, så opladning stoppes
    blue.value(1)  # Tænder for blåt lys

while True: # Program
    if ticks_ms() > threshold_update + starttime_update: # Nonblocking delay
        starttime_update = ticks_ms()
        print("Fetching data")
        co2 = int(fetch_green_power()) 
        if co2 < 50:
            led_green_power() # Grenn power func.
        else:
            led_no_green_power() # No green power func.
        print("Done")         
