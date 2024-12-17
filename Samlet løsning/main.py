from time import ticks_ms

#import ID1_main
import ID2_main
import ID6_main
##### Non blocking Delay Config #####
id2 = ticks_ms()
id6 = ticks_ms()
##### Non Blocking Delay timing #####
#Opgives i ms
id2timing = 5000
id6timing = 500
while True:
    if ticks_ms() > id2 + id2timing:
        id2 = ticks_ms() # Resetter nonblocking delay timer
        ID2_main.run()
    if ticks_ms() > id6 + id6timing:
        id6 = ticks_ms() + ID6_main.run() #Returnere positivt tal for at holde bremselyset tændt
        
    