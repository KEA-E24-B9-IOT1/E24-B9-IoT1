"""
Krav:
Når cyklen har stået stille i mere end 3 minutter,
og brugeren ikke har slukket permanent for løsningen,
sendes beskeder med cyklens placering til Thingsboard,
hvis cyklen kommer i bevægelse

Accepttest:
- Batteri skal være fuldt opladet
- Løsningen tændes
- En kort tur på 1 minut køres
- Cyklen stilles, men løsningen slukkes ikke, og tiden nulstilles
- Når der ikke er registreret bevægelse på cyklen i 3 minutter fra 3)
skal der inden for 30 sekunder komme en besked på Thingsboard hvis cyklen kommer i bevægelse,
og positionen sendes hvert tiende sekund til Thingsboard. Sker dette er kravet opfyldt.
"""

##### IMPORTS
import gc
import backend


##### VARIABLES AND CONSTANTS
gps_loc=[]

##### OBJECTS
gps = backend.gps

gps_loc_list=[]

##### PROGRAM
def is_moving():
    if gc.mem_free() < 2000:
        gc.collect()
    if gps.receive_nmea_data() and gps.get_validity()=="A":
        print("Bike gps")
        gps_loc={"Latitude":gps.get_latitude(),
                 "Longitude":gps.get_longitude()}
        gps_loc_list.append(gps_loc)
        if len(gps_loc_list)>180:
            del gps_loc_list[0]


def alarm():
    print("Alarmsystem check")
    if gc.mem_free() < 2000:
        gc.collect()
    if any(dictvalue1['Latitude']==gps.get_latitude() for dictvalue1 in gps_loc_list) and any(dictvalue2['Longitude']==gps.get_longitude() for dictvalue2 in gps_loc_list):
            print("Enabling alarm system")
            return True


def trigger_TB_alarm():
    print("TB alarm triggered")
    telemetry={"Latitude":gps.get_latitude(),"Longitude":gps.get_longitude()}
    return telemetry
