from time import ticks_ms

import ID1_main
import ID2_main
import ID6_main


##### Non blocking Delay Config #####
id1 = ticks_ms()
id2 = ticks_ms()
id3 = ticks_ms()
id4 = ticks_ms()
id5 = ticks_ms()
id6 = ticks_ms()


##### Non Blocking Delay timing #####
#Opgives i ms
id1timing = 300000
id2timing = 5000
# id3timing = None
# id4timing = None
# id5timing = None
id6timing = 500


##### Configs
ID1_main.run()


while True:
    if ticks_ms() > id1 + id1timing:
        id2 = ticks_ms()
        ID1_main.run()
    if ticks_ms() > id2 + id2timing:
        id2 = ticks_ms() # Resetter nonblocking delay timer
        ID2_main.run()
#     if ticks_ms() > id3 + id3timing:
#         Pass
#     if ticks_ms() > id4 + id4timing:
#         Pass
#     if ticks_ms() > id5 + id5timing:
#         Pass
    if ticks_ms() > id6 + id6timing:
        id6 = ticks_ms() + ID6_main.run() #Returnere positivt tal for at holde bremselyset tændt
