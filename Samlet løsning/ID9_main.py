"""
Man skal kunne sende en besked til løsningen fra Thingsboard så den aktiverer eller deaktiverer et alarmsystem så den blinker kraftigt med lys og giver lyd fra sig hvis den rykker sig når alarmen er slået til.
"""
import backend

def id_9_alarm(is_motion_detected):
    """Check main.py if bicycle should be noisy and flashy or not"""
    if is_motion_detected==True: # If bicycle has to be noisy and flashy
        backend.color_long(250,0,0) # Flashy neopixel ring
        backend.color_short(backend.rb,250,0,0) # Flashy right signal blinker
        backend.color_short(backend.lb,250,0,0) # Flashy left signal blinker
        backend.buzzer_PWM_objekt.freq(512) # Noisy tone
        backend.buzzer_PWM_objekt.duty(512) # Noisy volume
    if is_motion_detected==False: # If bicycle has to be quiet and non-flashy
        backend.color_long(0,0,0) # Not flashy
        backend.color_short(backend.rb,0,0,0) # Not flashy
        backend.color_short(backend.rb,0,0,0) # Not flashy
        backend.buzzer_PWM_objekt.duty(0) # Not noisy
