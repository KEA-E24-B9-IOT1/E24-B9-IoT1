import backend

average_current=[]

def ina_current_average():
    average_current.append(backend.ina_current())
    if len(average_current)>36:
        del average_current[0]
    avg_current=sum(average_current)/len(average_current)
    print(f"Avg current: {avg_current}")
    return avg_current

def est_batt_life():
    battlife=3600*(backend.batt_percentage()/100)/ina_current_average()
    telemetry = {'Battlife' : battlife}
    print(f"Est. batt life: {battlife}")
    backend.display(0, 0, "         ")
    backend.display(0, 0, f"Bat:{int(battlife)}T")
    return telemetry
    
