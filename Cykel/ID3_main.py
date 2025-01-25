import gc
import backend


def run():
    if gc.mem_free() < 2000: # free memory if below 2000 bytes left
        gc.collect()   # free memory 
    if backend.gps.receive_nmea_data() and backend.gps.get_validity()=="A":
        print("Valid gps data for TB")
        telemetry = {'Latitude': backend.gps.get_latitude(),
                        'Longitude': backend.gps.get_longitude(),
                        'Course' : backend.gps.get_course(),
                        'Speed' : backend.gps.get_speed(),
                        'Temperature' : backend.dht11_temp(),
                        'Batteri Percentage' : backend.batt_percentage()}
    if backend.gps.receive_nmea_data() and backend.gps.get_validity()=="V":
        print("Invalid gps data for TB")
        telemetry = {'Temperature' : backend.dht11_temp(),
                    'Batteri Percentage' : backend.batt_percentage()}
    return telemetry