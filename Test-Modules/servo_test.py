from machine import Pin, PWM
from time import sleep

# Define the servo pin
servo_pin = 0  # Replace with the actual pin connected to your servo

# Create a PWM object with 50Hz frequency
servo = PWM(Pin(servo_pin), freq=50) 

def set_servo_angle(angle):
    """
    Sets the servo angle to the specified value (0-180 degrees).
    """
    duty = int((angle / 180) * 1000)  # Convert angle to duty cycle
    servo.duty_u16(duty) 

# Open the servo 
set_servo_angle(90)
sleep(3)
# Wait a short time (adjust as needed)
# ...

# Close the servo
set_servo_angle(0)
sleep(3)