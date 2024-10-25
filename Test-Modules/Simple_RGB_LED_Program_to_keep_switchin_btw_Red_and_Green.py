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

# Example usage (replace with your RFID logic)
def process_rfid_signal(signal):
    #if signal == "specific_red_signal":
        show_red()
    #elif signal == "specific_green_signal":
        show_green()

# Main loop
while True:
    # Replace this with your actual RFID reading code
    #rfid_signal = input("Enter RFID signal (red/green): ")
    #process_rfid_signal(rfid_signal)
    show_red()
    show_green()