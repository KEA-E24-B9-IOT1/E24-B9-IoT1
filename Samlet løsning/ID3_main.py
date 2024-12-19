"""
Løsningen skal løbende sende data til ThingsBoard, der skal vise hastighed, retning, længde- og breddegrad, batteristatus og temperatur når cyklen er i brug. Hvis andet data måles skal det også præsenteres på Thingsboard.
"""
import gc
import backend


def run():
    """Upload valid data to Thingsboard"""
    backend.gps.receive_nmea_data()
    if gc.mem_free() < 2000: # free memory if below 2000 bytes left
        gc.collect()   # free memory 
    if backend.gps.receive_nmea_data(): # Is data available?
        if backend.gps.get_validity()=="A": # Is data validated?
            print("Valid gps data for TB") # For troubleshooting
            telemetry = {'Latitude': backend.gps.get_latitude(),
                         'Longitude': backend.gps.get_longitude(),
                         'Course' : backend.gps.get_course(),
                         'Speed' : backend.gps.get_speed(),
                         'Temperature' : backend.dht11_temp(),
                         'Batteri Percentage' : backend.batt_percentage()} # Save  gps and temp and batt data
        if backend.gps.get_validity()=="V": # Invalid gps data
            print("Invalid gps data for TB") # For troubleshooting
            telemetry = {'Temperature' : backend.dht11_temp(),
                       'Batteri Percentage' : backend.batt_percentage()} # Save temp and batt data
        return telemetry # Return telemetry to main.py for upload
