import requests
from time import ticks_ms
from machine import Pin

#Nonblocking delay config
threshold_update = 5000 #5 sek
starttime_update = ticks_ms() - threshold_update

threshold_clock = 1000 #5 sek
starttime_clock = ticks_ms() - threshold_update
#Så starter functionen med at hente data, fremfor at vente

#Pin Config
red_led = Pin(26, Pin.OUT)
yel_led = Pin(12, Pin.OUT)
gre_led = Pin(13, Pin.OUT)
relay = Pin(15, Pin.OUT)
#Opstart
red_led.value(0) #Slukker for rød
yel_led.value(0) #Tænder for gul
gre_led.value(0) #Slukker for grøn
relay.value(0)   #Slukker for relæ


def fetch_green_power():
    response = requests.get(
        url = "https://api.energidataservice.dk/dataset/CO2Emis?limit=2")

    co2emis = response.json().get('records')[1].get('CO2Emission')
    co2emis = 51
    if co2emis == None:
        return 0
    return co2emis
def led_green_power():
    gre_led.value(1) #Tænder for grøn LED
    yel_led.value(1) #Fungere omvendt. Slukker
    red_led.value(0) #Slukker for rød LED
    relay.value(1) #Tænder for relæ, så opladning startes
def led_no_green_power():
    gre_led.value(0) #Tænder for grøn LED
    yel_led.value(1) #Fungere omvendt. Slukker
    red_led.value(1) #Slukker for rød LED
    relay.value(0) #slukker for relæ, så opladning stoppes
while True:
    if ticks_ms() > threshold_update + starttime_update:
        starttime_update = ticks_ms()
        print("Fetching data")
        co2 = fetch_green_power()
        if co2 == 0:
            yel_led.value(0) #Hopefully this never runs
        if co2 < 50:
            led_green_power() #Grenn power func.
        else:
            led_no_green_power() #No green power func.
        print("Done")
    if ticks_ms() > threshold_clock + starttime_clock:
        starttime_clock = ticks_ms()
        print(".")
            
            