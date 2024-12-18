##### IMPORTS
from time import ticks_ms
import backend


right_blinker=backend.rb
right_button=backend.right_button
backend.color_short(right_blinker,0,0,0)

left_blinker=backend.lb
left_button=backend.left_button
backend.color_short(left_blinker,0,0,0)


def left_blinker_func():
    print("Running left blinker")
    timer=ticks_ms()
    counter = 1
    while True:
        if counter == 1 or counter == 3 or counter == 5:
            backend.color_short(left_blinker,250,75,0)
            if ticks_ms()-timer>500:
                timer=ticks_ms()
                counter += 1
        if counter == 2 or counter == 4 or counter == 6:
            backend.color_short(left_blinker,0,0,0)
            if ticks_ms()-timer>500:
                timer=ticks_ms()
                counter += 1
        if counter > 6:
            print("Breaking left blinker")
            break

def right_blinker_func():
    print("Running right blinker")
    timer=ticks_ms()
    counter=1
    while True:
        if counter == 1 or counter == 3 or counter == 5:
            backend.color_short(right_blinker,200,75,0)
            if ticks_ms()-timer>500:
                timer=ticks_ms()
                counter += 1
        if counter == 2 or counter == 4 or counter == 6:
            backend.color_short(right_blinker,0,0,0)
            if ticks_ms()-timer>500:
                timer=ticks_ms()
                counter += 1
        if counter > 6:
            print("Breaking left blinker")
            break