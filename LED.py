import RPi.GPIO as GPIO
import time
import numpy as np

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)



LED_PIN = 26     # output pin on the raspberry pi

GPIO.setup(LED_PIN, GPIO.OUT)       

# GPIO.output(LED_PIN, GPIO.LOW)
# GPIO.output(LED_PIN, GPIO.HIGH)

# turn on:
GPIO.output(LED_PIN, 0)

time.sleep(1)

t0 = time.time()


blink_rate = 10         # hz 
period = 1/blink_rate 
# blink_rate*period = 1   -->   period = 1/blink_rate 


duration_lim = 4           # duration of the whole thing

on = False
done = False
while not done:

    if not on: 
        # turn on if off:
        GPIO.output(LED_PIN, 1)
        on = True

    elif on:
        # turn off if on:
        GPIO.output(LED_PIN, 0)
        on = False


    time.sleep(period/2)

    t = time.time()
    duration = t - t0

    if duration >= duration_lim:
        done = True
        
GPIO.cleanup()

    


# turn off:
#GPIO.output(LED_PIN, 0)

#GPIO.output(LED_PIN, GPIO.HIGH)



#time.sleep(2)
#while True:
#    GPIO.output(LED_PIN, GPIO.HIGH)
#    time.sleep(0.3)
#
#    GPIO.output(LED_PIN, GPIO.LOW)
#    time.sleep(0.3)


