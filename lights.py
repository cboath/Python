#!/usr/bin/python
import RPi.GPIO as GPIO
import threading
import time
import random

R = 16
G = 12
B = 13

PINS = [R, G, B]

def initialize_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(PINS, GPIO.OUT, initial=GPIO.LOW)

def color_test(channel, frequency, speed, step):
    p = GPIO.PWM(channel, frequency)
    p.start(0)
    for x in range(3):
        for dutyCycle in range(0, 101, step):
            p.ChangeDutyCycle(dutyCycle)
            time.sleep(speed)
        for dutyCycle in range(100, -1, -step):
            p.ChangeDutyCycle(dutyCycle)
            time.sleep(speed)

def main():
    try:
        initialize_gpio()
        threads = []
        threads.append(threading.Thread(target=color_test, args=(G, 300, 0.02, 5)))
        threads.append(threading.Thread(target=color_test, args=(R, 300, 0.02, 5)))
        threads.append(threading.Thread(target=color_test, args=(B, 300, 0.02, 5)))
        for t in threads:
            t.start()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print
        print('bye.')

if __name__ == '__main__':
    main()
