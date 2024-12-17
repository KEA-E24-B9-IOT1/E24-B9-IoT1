import gc
import secrets
import backend
from uthingsboard.client import TBDeviceMqttClient
from time import ticks_ms


ina=backend.ina


average_current=[]


def ina_current_average():
    average_current.append(backend.ina_current())
    if len(average_current)>36:
        del average_current[0]
    avg_current=sum(average_current)/len(average_current)
    return avg_current

def est_batt_life():
    battery_percentage=backend.batt_percentage()
    battlife=3600*(backend.batt_percentage()/100)/ina_current_average()
    telemetry = {'Battlife' : battlife}
    return telemetry
    
