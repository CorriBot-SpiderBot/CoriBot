# Import libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(11,GPIO.OUT)
#GPIO.setup(13,GPIO.OUT)

servo1 = GPIO.PWM(11,50)
# Note 11 is pin, 50 = 50Hz pulse
#servo2 = GPIO.PWM(13,50)
#start PWM running, but with value of 0 (pulse off)
servo1.start(0)
#servo2.start(0)
print ("Waiting for 2 seconds")
time.sleep(2)
# Loop for duty values from 2 to 12 (0 to 180 deg
# Turn back to 90 degrees
print ("Turning back to 90 degrees for 2 seconds")
servo1.ChangeDutyCycle(2)

#servo2.ChangeDutyCycle(8)
time.sleep(2)

#Clean things up at the end
servo1.stop()
GPIO.cleanup()
print ("Goodbye")
