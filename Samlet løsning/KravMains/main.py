from time import ticks_ms

#import ID1_main
import ID2_main

##### Non blocking Delay Config #####
id2 = ticks_ms()
##### Non Blocking Delay timing #####
#Opgives i ms
id2timing = 1000

while True:
    if ticks_ms() > id2 + id2timing:
        id2 = ticks_ms() # Resetter nonblocking delay timer
        ID2_main.run()
        print("ID2_main")
    