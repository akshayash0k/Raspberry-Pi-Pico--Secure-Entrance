from machine import Pin
import utime

buzzer_pin = Pin(14, Pin.OUT)

def beep(duration):
        buzzer_pin.high()
        utime.sleep(duration)
        buzzer_pin.low()
        

beep(0.5)  #  Make a short beep for 0.5 seconds
utime.sleep(1)  # Add a pause
beep(0.5)