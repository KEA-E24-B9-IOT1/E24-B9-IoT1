"""
Der skal være blinklys på hver side af cyklen, som skal kunne aktiveres og deaktiveres lokalt på cyklen.
"""

##### IMPORTS
from time import ticks_ms # For non-blocking blinking
import backend


backend.color_short(backend.rb,0,0,0) # Start with turning off neopixel lights

backend.color_short(backend.lb,0,0,0) # Start with turning off neopixel lights


def left_blinker_func():
    """Make left neopixel strip blink as a signal light"""
    print("Running left blinker") # For troubleshooting
    timer=ticks_ms() # Non-blocking delay for manipulating light
    counter = 1 # Counter for on/off-cycle
    while True: # Mali's bedste ven
        if counter == 1 or counter == 3 or counter == 5: # On-cycle
            backend.color_short(backend.lb,250,75,0) # Call backend-function to manipulate light
            if ticks_ms()-timer>500: # Non-blocking delay to increase counter and alternate on/off-cycle
                timer=ticks_ms()
                counter += 1
        if counter == 2 or counter == 4 or counter == 6: # Off-cycle
            backend.color_short(backend.lb,0,0,0) # Call backend-function to manipulate light
            if ticks_ms()-timer>500:
                timer=ticks_ms()
                counter += 1
        if counter > 6: # End signal after 3 full on/off cycles
            print("Breaking left blinker") # For troubleshooting
            break

def right_blinker_func():
    """Everything from left_blinker_func applies heres as well"""
    print("Running right blinker")
    timer=ticks_ms()
    counter=1
    while True:
        if counter == 1 or counter == 3 or counter == 5:
            backend.color_short(backend.rb,250,75,0)
            if ticks_ms()-timer>500:
                timer=ticks_ms()
                counter += 1
        if counter == 2 or counter == 4 or counter == 6:
            backend.color_short(backend.rb,0,0,0)
            if ticks_ms()-timer>500:
                timer=ticks_ms()
                counter += 1
        if counter > 6:
            print("Breaking left blinker")
            break
