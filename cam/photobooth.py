import picamera
from time import sleep
import RPi.GPIO as GPIO
import pygame
from pygame.locals import *

##GPIO.setmode(GPIO.BCM)
##GPIO.setwarnings(False)
##GPIO.setup(17,GPIO.IN,GPIO.PUD_UP)
##GREEN_LED = 22
##GPIO.setup(GREEN_LED, GPIO.OUT)

pygame.init()
black = 0,0,0
white = 255,255,255
infoObject = pygame.display.Info()
newWidth = infoObject.current_w
newHeight = infoObject.current_h
windowSize = width, height = newWidth, newHeight
screen = pygame.display.set_mode(windowSize)
myfont = pygame.font.Font(None, 600)
labelPOS = (newWidth / 2, newHeight / 3)
transparent = 0,0,0,0

with picamera.PiCamera() as camera:
      camera.rotation = 180
      camera.start_preview()
      screen.fill(black)
      camera.preview.alpha = 128
      #GPIO.wait_for_edge(17, GPIO.FALLING)
      shot = 0
      while shot < 2:
            #GPIO.output(GREEN_LED,True)
            for x in range (4, 0 , -1):
                 label = myfont.render(str(x),1,white)
                 screen.blit(label, labelPOS)
                 sleep(1)
                 pygame.display.flip()
                 screen.fill(transparent)
            #GPIO.output(GREEN_LED,False)
            camera.capture('img{counter:02d}.jpg')
            shot += 1
      camera.stop_preview()
      pygame.display.quit()
      pygame.quit()
