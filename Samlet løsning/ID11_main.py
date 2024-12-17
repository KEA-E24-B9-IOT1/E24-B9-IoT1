##### IMPORTS
from time import ticks_ms,sleep
import backend


right_blinker=backend.rb
right_button=backend.right_button
backend.color_short(right_blinker,0,0,0)

left_blinker=backend.lb
left_button=backend.left_button
backend.color_short(left_blinker,0,0,0)


def left_blinker_func(ticks):
    backend.color_short(left_blinker,0,0,0)
    

def run(left_counter,right_counter):
    if left_counter > 0 and nonblocking delay:
        backend.color_short(left_blinker,0,0,0)
        
    
