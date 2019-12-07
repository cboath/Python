# VCC goes to pin 2
# GND goes to pin 6
# DO goes to pin 40
# AO not used


import RPi.GPIO as GPIO
import time

channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    print(callback)
    if GPIO.input(channel):
       print("No water detected")
    else:
       print("Water detected")
       
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)
       
while True:
       time.sleep(1)
