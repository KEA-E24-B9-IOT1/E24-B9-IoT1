from uthingsboard.client import TBDeviceMqttClient
import gc
import secrets
import backend


def run():
    if gc.mem_free() < 2000: # free memory if below 2000 bytes left
        gc.collect()   # free memory 
    if backend.gps.receive_nmea_data():
        if backend.gps.get_validity()=="A":
            telemetry = {'Latitude': backend.gps.get_latitude(),
                         'Longitude': backend.gps.get_longitude(),
                         'Course' : backend.gps.get_course(),
                         'Speed' : backend.gps.get_speed(),
                         'Temperature' : backend.dht11_temp(),
                         'Batteri Percentage' : backend.batt_percentage()}
        if backend.gps.get_validity()=="V":
            telemetry = {'Temperature' : backend.dht11_temp(),
                       'Batteri Percentage' : backend.batt_percentage()}
        return telemetry