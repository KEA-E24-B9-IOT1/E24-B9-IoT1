from machine import ADC, Pin, PWM
from time import sleep
from adc_sub import ADC_substitute

# Denne kode er udviklet til breadboard

pin_adc=34

esp_adc = ADC_substitute(pin_adc)

while True:
    Spænding = esp_adc.read_voltage()*2         # Gange 2 eftersom, vi har halveret den reéle batterispænding
    batteriprocent=((Spænding-3)/(4.2-3-0))*100
    print("Batterispænding:", Spænding, "V")
    print(f"Batteriprocent: {batteriprocent}%")
    sleep(0.5)


