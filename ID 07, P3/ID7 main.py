from time import ticks_ms
import backend

ina=backend.ina

ina_ticker=ticks_ms()
average_current=[]

while True:
    if ticks_ms()-ina_ticker>1000:
        """Mål batteriprocent"""
        battery_percentage=batter_procent_function(ina.get_bus_voltage)
        """Mål strømforbrug"""
        batt_current=ina.get_current()
        """Hav en liste over strømforbrug fra de sidste 3 timer"""
        current_list.append(batt_current)
        """Mål hvert sekund"""
            """3600 målinger for 1 time??"""
                """10800 målinger for 3 timer"""
                    """Er det plausibelt?"""
        """Begræns listen til maksimalt 10800 målinger"""
            if len(current_list)>10800:
                del current_list[0]
        """Find gennemsnit af målingerne"""
        average_current=sum(current_list)/len(current_list)
        
        """Udregn rest. levetid ud fra ina-målinger"""
        """Kapacitet er 3600mAh"""
        """Nominalspænding er 7.4V, men spænd er fra 6V til 8.4V"""            