#!/usr/bin/env python

#required to run  sudo pip3 install rpi_wsx281x

#wiring setup
#5v - pin 2 - red wire on lights
#ground - pin 6 - white wire on lights
#data - pin 12 - green wire on lights (middle)

# stringRunner
# runs pixels through an LED string
# designed by David Guidos, August 2017
#
# control pin for string is GPIO 18
import atexit
import time
import RPi.GPIO as GPIO
import random

from rpi_ws281x import __version__, PixelStrip, Color

# LED strip configuration:
LED_COUNT      = 288      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal
LED_BRIGHTNESS = 128     # Set to 0 for darkest and 255 for brightest
LED_CHANNEL    = 0       # PWM channel
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_GAMMA = [
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2,
2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5,
6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 11, 11,
11, 12, 12, 13, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18,
19, 19, 20, 21, 21, 22, 22, 23, 23, 24, 25, 25, 26, 27, 27, 28,
29, 29, 30, 31, 31, 32, 33, 34, 34, 35, 36, 37, 37, 38, 39, 40,
40, 41, 42, 43, 44, 45, 46, 46, 47, 48, 49, 50, 51, 52, 53, 54,
55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
71, 72, 73, 74, 76, 77, 78, 79, 80, 81, 83, 84, 85, 86, 88, 89,
90, 91, 93, 94, 95, 96, 98, 99,100,102,103,104,106,107,109,110,
111,113,114,116,117,119,120,121,123,124,126,128,129,131,132,134,
135,137,138,140,142,143,145,146,148,150,151,153,155,157,158,160,
162,163,165,167,169,170,172,174,176,178,179,181,183,185,187,189,
191,193,194,196,198,200,202,204,206,208,210,212,214,216,218,220,
222,224,227,229,231,233,235,237,239,241,244,246,248,250,252,255]    
ws2812 = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_GAMMA)
ws2812.begin()

_pixels = [(0,0,0) for x in range(LED_COUNT)]

def clear():
    """Clear the buffer"""
    for x in range(LED_COUNT):
        ws2812.setPixelColorRGB(x, 0, 0, 0)
        _pixels[x] = (0, 0, 0)

# run a single pixel through the string
# direction 0 goes from start to end, 1 goes end to start
def runString(pixelColor, direction):
 rMin = 0
 rMax = LED_COUNT
 if direction == 0:
     direction = -1
     rMax = 0
     rMin = LED_COUNT
     
 for n in range(rMin, rMax, direction):
   # set the pixel  
   (r, g, b) = pixelColor
   ws2812.setPixelColorRGB(n, r, g, b)
ws2812.show()
   # small delay
   #time.sleep(0.002)

try:
    while True:
     for n in range(0, LED_COUNT):
       # set the pixel  
       #(r, g, b) = pixelColor
       ws2812.setPixelColorRGB(n, random.randint(0,255), random.randint(0,255), random.randint(0,255))
     ws2812.show()
       # small delay
       #time.sleep(0.002)
        
    while True:
     c = 0  # color pointer
     rLoop = 0
     gLoop = 0
     bLoop = 0
     
     # loop
     for lap in range(3):
       # color list
       #pixelColor = [(rLoop, bLoop, cLoop), (rLoop, bLoop, cLoop), (rLoop, bLoop, cLoop)]
       pixelColor = [(255, 255, 0), (125, 225, 130), (150, 0, 255)]
       # swap direction
       for direction in range(2):
         #print(lap, direction)
         runString(pixelColor[c % 3], direction)
         #runString(pixelColor[random.randint(0, 2)], direction)
         c += 1
         
except KeyboardInterrupt:
    clear()
    ws2812.show()
