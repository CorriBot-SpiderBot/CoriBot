from __future__ import division
import time

import Adafruit_PCA9685

pwm1 = Adafruit_PCA9685.PCA9685(address=0x40)
pwm2 = Adafruit_PCA9685.PCA9685(address=0x41)

servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm1.set_pwm(channel, 0, pulse)
    pwm2.set_pwm(channel, 0, pulse)

pwm1.set_pwm_freq(60)
pwm2.set_pwm_freq(60)

print('Moving servo on channel, press Ctrl-C to quit...')
#while true:

pwm2.set_pwm(5, 0, 150)
pwm2.set_pwm(4, 0, 150)
pwm1.set_pwm(7, 0, 280)
pwm1.set_pwm(8, 0, 230)
pwm1.set_pwm(2, 0, 250)
pwm1.set_pwm(1, 0, 230)
time.sleep(1)

pwm2.set_pwm(3, 0, 330)
time.sleep(1)

pwm2.set_pwm(4, 0, 250)
pwm1.set_pwm(0, 0, 420)
pwm1.set_pwm(2, 0, 150)
time.sleep(1)

pwm1.set_pwm(4, 0, 200)
pwm2.set_pwm(1, 0, 200)
pwm2.set_pwm(7, 0, 200)
time.sleep(1)
pwm1.set_pwm(0, 0, 400)
pwm1.set_pwm(1, 0, 250)
pwm1.set_pwm(7, 0, 250)
pwm1.set_pwm(8, 0, 150)
pwm2.set_pwm(3, 0, 400)