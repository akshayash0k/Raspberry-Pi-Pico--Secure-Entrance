from machine import Pin
import time

# Set up the RGB LED pin
led_pin = Pin(22, Pin.OUT)

def led_on():
    """Turn the LED on"""
    led_pin.value(1)

def led_off():
    """Turn the LED off"""
    led_pin.value(0)

def blink_led(duration):
    """Blink the LED for the specified duration"""
    led_on()
    time.sleep(duration)
    led_off()

def process_rfid_signal(signal):
    #if signal == "specific_red_signal":
        blink_led(1)  # Blink for 1 second
    #elif signal == "specific_green_signal":
        blink_led(0.5)  # Blink for 0.5 seconds

# Main loop
while True:
    # Replace this with your actual RFID reading code
    #rfid_signal = input("Enter RFID signal (red/green): ")
    #process_rfid_signal(rfid_signal)
    blink_led(1)