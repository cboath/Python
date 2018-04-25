import sys
import RPi.GPIO as GPIO
from time import sleep
import os

pinuse = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinuse, GPIO.IN)

def noisy(counter):
    duration = 1
    freq = (counter % 3) * 400
    if freq == 0:
        freq = 1200
    print('Frequency =', freq)
    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))

def motionSensor(pinuse):    
    global counter
    counter += 1
    noisy(counter)
    print('Motion detected\n{0}'.format(counter))

try:
    GPIO.add_event_detect(pinuse, GPIO.RISING, callback=motionSensor)
    counter = 0
    
    while True:
        sleep(0.1)
        
except:
    GPIO.cleanup()
    print('All done')
    
#sudo apt-get install sox    
