"""
Der skal være blinklys på hver side af cyklen, som skal kunne aktiveres og deaktiveres lokalt på cyklen.
"""

##### IMPORTS
from time import ticks_ms # For non-blocking blinking
import backend


backend.color_short(backend.rb,0,0,0) # Start with turning off neopixel lights
backend.color_short(backend.lb,0,0,0) # Start with turning off neopixel lights


leftcounter = 0
rightcounter = 0
timer = 0


def blinker():
    global timer
    if ticks_ms() > timer + 450:
        global leftcounter
        global rightcounter
        if leftcounter > 0:
            if leftcounter % 2 == 0: # True if Even, hvis der ikke er nogen rest efter modulo, så er tallet lige
                backend.color_short(backend.lb,250,75,0) # Call backend-function to manipulate light
            if leftcounter % 2 != 0: # False if Even, hvis der er en rest efter modulo, så er tallet ulige
                backend.color_short(backend.lb,0,0,0) # Call backend-function to manipulate light
            print("ID11 leftcounter : ", leftcounter)
            leftcounter -= 1
        if rightcounter > 0:
            if rightcounter % 2 == 0:
                backend.color_short(backend.rb,250,75,0)
            if rightcounter % 2 != 0:
                backend.color_short(backend.rb,0,0,0)
            print("ID11 rightcounter: ", rightcounter)
            rightcounter -= 1
        timer = ticks_ms()
        
def left_blinker_func():
    global leftcounter
    leftcounter = 6
    """Make left neopixel strip blink as a signal light"""
    print("Running left blinker") # For troubleshooting

def right_blinker_func():
    global rightcounter
    rightcounter = 6
    """Everything from left_blinker_func applies heres as well"""
    print("Running right blinker")