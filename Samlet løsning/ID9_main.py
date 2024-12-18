"""
ID 9
Man skal kunne sende en besked til løsningen fra Thingsboard,
så den aktiverer eller deaktiverer et alarmsystem,
så den blinker kraftigt med lys og giver lyd fra sig,
hvis den rykker sig når alarmen er slået til.
"""
import backend

##### CONFIGURATIONS
alarm_triggered=False
alarm_enabled=False


def trigger_alarm(): #Farvefunktion til NeoPixels & Buzzer
    alarm_ticker = ticks_ms()
    alarm_noise=True
    if ticks_ms() - alarm_ticker > 1000:
        if alarm_noise == True:
            backend.color_long(250,0,0)
            backend.color_short(backend.rb,250,0,0)
            backend.color_short(backend.lb,250,0,0)
            backend.buzzer_PWM_objekt.freq(1023)
            backend.buzzer_PWM_objekt.duty(512)
            alarm_ticker = ticks_ms()
            alarm_noise = False
        if alarm_noise == False:
            backend.color_long(0,0,0)
            backend.color_short(backend.rb,0,0,0)
            backend.color_short(backend.rb,0,0,0)
            backend.buzzer_PWM_objekt.freq(512)
            backend.buzzer_PWM_objekt.freq(512)
            alarm_ticker = ticks_ms()
            alarm_noise = True

# def handler(req_id, method, params):
#     """Handler callback to receive RPC from server"""
#     print(f"Response: {req_id}: {method}, params {params}")
#     print(params, "params type:", type(params))
#     try:
#         if method=="Enable alarm":
#             if params==True:
#                 print("Alarm enabled")
#                 global alarm_enabled=True
#             elif params==False:
#                 print("Alarm disabled")
#                 global alarm_enabled=False
#     except TypeError as e:
#         print(e)


def id_9_alarm():
    if alarm_enabled==True:
        values = backend.mpu.get_values() #Henter værdier fra MPU
        if  values["acceleration x"] < -1000: # Tænd for alarm hvis
            alarm_triggered=True
        if values["acceleration x"] > -1000: # Deaktiver lys og lyd
            alarm_triggered=False

        if alarm_triggered==False:
            disable_active_alarm()
        if alarm_triggered==True:
            trigger_alarm(255,0,0) #Funktion kaldes

    if alarm_enabled==False:
        alarm_triggered=False
        backend.color_long(0,0,0)
        backend.color_short(backend.rb,0,0,0)
        backend.color_short(backend.rb,0,0,0)
        backend.buzzer_PWM_objekt.duty(0)
