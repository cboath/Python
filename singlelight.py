#!/usr/bin/python
import RPi.GPIO as GPIO
import threading
import time
import random

R = 16
G = 12
B = 13

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(R, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)

rvalue = input("Red value: ")
gvalue = input("Green value: ")
bvalue = input("Blue value: ")

freq = 300

redlight = GPIO.PWM(R, freq)
bluelight = GPIO.PWM(B, freq)
greenlight = GPIO.PWM(G, freq)

x=1
while x == 1:
    redlight.start(rvalue)
    bluelight.start(bvalue)
    greenlight.start(gvalue)
    raw_input("Press any key:")
    x = 0

GPIO.cleanup()
