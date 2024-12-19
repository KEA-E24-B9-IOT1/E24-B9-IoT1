"""
Bremselys skal lyse når der bremses over en valgfri negativ acceleration
"""
import backend

def run():
    """Turn on brake lights if negative acceleration"""
    values = backend.mpu.get_values() # Fetch values from MPU
    if  values["acceleration y"] > 1000: # Check if value for y-axis is greater than 1000
        backend.color_long(255,0,0) # Call function from backend, to manipulate neopixel ring
        print("Tænd neopixel ring") # For troubleshooting
        return 1000 # Return amount of time the light has to be on. Must be incorporated into the non-blocking delay so it doesn't wrongfully get called again.
    else:
        backend.color_long(0,0,0)   # Same function as above, but to turn off neopixels
        print("Sluk neopixel ring") # For troubleshooting
        return 0 # No delay
        
