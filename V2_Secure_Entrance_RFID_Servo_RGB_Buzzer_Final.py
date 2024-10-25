from machine import Pin, PWM
from mfrc522 import MFRC522
import neopixel
import time
from time import sleep
import utime

# Set up the NeoPixel RGB LED
led_count = 1
led_pin = 10   # Connected to GP10
np = neopixel.NeoPixel(Pin(led_pin), led_count)

def set_color(r, g, b):
    """Set the RGB LED color (0-255 for each component)"""
    np[0] = (r, g, b)
    np.write()

def show_color(r, g, b, duration=1):
    """Show a color for a specified duration"""
    set_color(r, g, b)
    time.sleep(duration)
    set_color(0, 0, 0)  # Turn off LED

def turn_off_led():
    """Turn off the RGB LED"""
    set_color(0, 0, 0)

# Setup the buzzer
buzzer = PWM(Pin(14))

def buzzer_sound(freq, duration):
    buzzer.freq(freq)
    buzzer.duty_u16(3000)  # Adjust this value for loudness
    time.sleep(duration)
    buzzer.duty_u16(0)

# Set up PWM Pin for servo control
servo_pin = machine.Pin(0)
servo = PWM(servo_pin)

# Set Duty Cycle for Different Angles
max_duty = 7864  # Maximum Pulse Width (180º) corresponds to 7864
min_duty = 1802  # Minimum Pulse Width (0º) corresponds to 1802
half_duty = int(max_duty/2)

# Set PWM frequency
frequency = 50
servo.freq(frequency)

def move_servo(angle):
    """Move servo to specified angle"""
    duty = int(min_duty + (angle / 180) * (max_duty - min_duty))
    servo.duty_u16(duty)

reader = MFRC522(spi_id=0, sck=6, miso=4, mosi=7, cs=5, rst=22)

print("Bring RFID TAG Closer...")
print("")

# Dictionary of authorized cards
authorized_cards = {
    810107747: {"status": "AUTHORIZED", "color": "GREEN", "angle": 90},
    229639603: {"status": "DENIED", "color": "RED", "angle": 0}
}

def handle_card(card_id):
    if card_id in authorized_cards:
        card_info = authorized_cards[card_id]
        status = card_info["status"]
        color = card_info["color"]
        angle = card_info["angle"]
        
        print(f"Card ID: {card_id} - {status}")
        
        if status == "AUTHORIZED":
            show_color(0, 255, 0)  # Green light
            buzzer_sound(1000, 0.4)
            buzzer_sound(1200, 0.4)
            move_servo(angle)
            print("Access granted. Door opening.")
            sleep(3)
            move_servo(0)  # Close the door
        else:
            show_color(255, 0, 0)  # Red light
            buzzer_sound(300, 0.5)
            buzzer_sound(200, 0.5)
            print("Access denied. Wrong card.")
    else:
        print(f"Card ID: {card_id} - UNAUTHORIZED: NO CARDS DETECTED")
        show_color(255, 255, 0)  # Yellow for unauthorized
        buzzer_sound(200, 0.8)  # Different sound for unauthorized
        print("Unauthorized card. Access denied.")

while True:
    try:
        reader.init()
        (stat, tag_type) = reader.request(reader.REQIDL)
        if stat == reader.OK:
            (stat, uid) = reader.SelectTagSN()
            if stat == reader.OK:
                card = int.from_bytes(bytes(uid), "little", False)
                handle_card(card)
    except Exception as e:
        print(f"An error occurred: {e}")
    
    turn_off_led()
    sleep(0.1)  # Small delay to prevent tight looping
