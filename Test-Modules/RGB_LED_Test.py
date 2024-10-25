from machine import Pin
import neopixel
import time

# Set up the NeoPixel RGB LED
led_count = 1  # Assuming you have one RGB LED
led_pin = 22   # Connected to GP22
np = neopixel.NeoPixel(Pin(led_pin), led_count)

def set_color(r, g, b):
    """Set the RGB LED color (0-255 for each component)"""
    np[0] = (r, g, b)
    np.write()
    
def show_red():
    """Show red color for 1 second"""
    set_color(255, 0, 0)
    time.sleep(1)
    set_color(0, 0, 0)  # Turn off LED
        
def show_green():
    """Show green color for 1 second"""
    set_color(0, 255, 0)
    time.sleep(1)
    set_color(0, 0, 0)  # Turn off LED

def turn_off_led():
    """Turn off the RGB LED"""
    set_color(0, 0, 0)
    

#Main Loop
while True:
    show_red()
    show_green()
    turn_off_led()