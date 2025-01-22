"""
ID 9
Man skal kunne sende en besked til løsningen fra Thingsboard,
så den aktiverer eller deaktiverer et alarmsystem,
så den blinker kraftigt med lys og giver lyd fra sig,
hvis den rykker sig når alarmen er slået til.
"""
import backend

def id_9_alarm(is_motion_detected):
    if is_motion_detected==True:
        backend.color_long(250,0,0)
        backend.color_short(backend.rb,250,0,0)
        backend.color_short(backend.lb,250,0,0)
        backend.buzzer_PWM_objekt.freq(512)
        backend.buzzer_PWM_objekt.duty(512)
    if is_motion_detected==False:
        backend.color_long(0,0,0)
        backend.color_short(backend.rb,0,0,0)
        backend.color_short(backend.rb,0,0,0)
        backend.buzzer_PWM_objekt.duty(0)
