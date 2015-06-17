import RPi.GPIO as GPIO
import time

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Configuration for a Raspberry Pi:
GPIO_PIR = 12  # GPIO 12, Pin# 32

# set pin as input
GPIO.setup(GPIO_PIR, GPIO.IN)

preState = 0
currState = 0

def motion(gpio):
    global preState
    global currState

    currState = GPIO.input(gpio)

    if preState == 0 and currState == 1: 
        print "Motion Detected"
    elif preState == 1 and currState == 0:
        print "Ready"

    preState = currState

try:
    GPIO.add_event_detect(GPIO_PIR, GPIO.BOTH, callback=motion)
    while 1:
        time.sleep(100)

except KeyboardInterrupt:
    print "  ---> Quit"
    GPIO.cleanup()
