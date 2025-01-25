import backend

mpu = backend.mpu #MPU

def run():
    values = mpu.get_values() #Henter værdier fra MPU
    if  values["acceleration y"] > 1000: # Tænder for bremselys, hvis over 1000
        backend.color_long(255,0,0) #Funktion kaldes
        #print("Tænd neopixel ring")
        return 1000 #return mængden af tid bremselyset skal være tændt. Dette skal inkoporeres i non-blocking delay,
                    #så denne ikke kalder functionen igen og potentielt slukker for bremselyset
    else:
        backend.color_long(0,0,0)   #Funktion kaldes
        #print("Sluk neopixel ring")
        return 0
        