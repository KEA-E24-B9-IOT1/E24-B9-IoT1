"""
This is a template for our .py files,
to ensure a similar and streamlined construction.
"""

##### IMPORTS
from machine import Pin
from time import ticks_ms,sleep


##### PINS
# TILRET PINS TIL DE REELLE PINS I KREDSLØBET!
## DISSE PINS ER FRA EDUCABOARDET!
left_blinker_pin=26
left_button_pin=4

right_blinker_pin=12
right_button_pin=0


##### CONFIGURATIONS
time_ticker=ticks_ms()
blinker_ticker=ticks_ms()
blink_left=False
blink_right=False

##### OBJECTS
right_blinker=Pin(right_blinker_pin,Pin.OUT)
right_button=Pin(right_button_pin,Pin.IN)
right_blinker.off()

left_blinker=Pin(left_blinker_pin,Pin.OUT)
left_button=Pin(left_button_pin,Pin.IN)
left_blinker.off()

##### FUNCTIONS



##### PROGRAM
while True:
    left_first=left_button.value()
    right_first=right_button.value()
    sleep(0.1)
    left_second=left_button.value()
    right_second=right_button.value()
    if left_first==1 and left_second==0:
        blink_left=True
        left_blinker.value(not left_blinker.value())
        blink_right=False
        right_blinker.off()
    if right_first==1 and right_second==0:
        blink_right=True
        right_blinker.value(not right_blinker.value())
        blink_left=False
        left_blinker.off()
    if blink_left==True:
        if ticks_ms()-blinker_ticker>500:
            left_blinker.value(not left_blinker.value())
            blinker_ticker=ticks_ms()
    if blink_right==True:
        if ticks_ms()-blinker_ticker>500:
            right_blinker.value(not right_blinker.value())
            blinker_ticker=ticks_ms()