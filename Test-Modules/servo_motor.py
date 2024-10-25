from machine import Pin, PWM
from time import sleep

# Set up PWM Pin for servo control
servo_pin = machine.Pin(0)
servo = PWM(servo_pin)

# Set Duty Cycle for Different Angles
max_duty = 7864 #Maximum Pulse Width (180º) corresponds to 7864
min_duty = 1802 #Minimum Pulse Width (0º) corresponds to 1802
half_duty = int(max_duty/2)

#Set PWM frequency
frequency = 50
servo.freq (frequency)

try:
    while True:
        #Servo at 0 degrees
        servo.duty_u16(min_duty)
        print("Servo at 0 degrees, min_duty = 1802")
        sleep(3)
        
        #Servo at 90 degrees
        servo.duty_u16(half_duty)
        print("Servo at 90 degrees, half_duty")
        sleep(3)
        
        #Servo at 180 degrees
        #servo.duty_u16(max_duty)
        #print("Servo at 180 degrees, max_duty = 7864")
        # sleep(3)    
      
except KeyboardInterrupt:
    print("Keyboard interrupt")
    # Turn off PWM 
    servo.deinit()