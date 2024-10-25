from machine import Pin, PWM
import time

buzzer = PWM(Pin(14))

def buzzer_sound(freq, duration):
    buzzer.freq(freq)
    buzzer.duty_u16(3000)  # Adjust this value for loudness
    time.sleep(duration)
    buzzer.duty_u16(0)
    
    
buzzer_sound(400, 0.2)  # Sound 1 when opening the door
buzzer_sound(600, 0.2)   # Sound 2 when closing the door