import picamera
from picamera import Color
from time import sleep
import RPi.GPIO as GPIO
import pygame

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
newHeight = infoObject.current_h - 100
windowSize = width, height = newWidth, newHeight
screen = pygame.display.set_mode(windowSize)
myfont = pygame.font.Font(None, 600)
labelPOS = (newWidth / 2, newHeight / 3)

with picamera.PiCamera() as camera:
      camera.rotation = 180
      camera.resolution = (1280, 768)
      camera.start_preview(fullscreen=False, window = (150, 110, 1680, 1050))
      camera.annotate_text_size = 45
      camera.annotate_background = Color('white')
      camera.annotate_foreground = Color('green')
      camera.annotate_text = 'Daugherty SA&E Summit 2019'
      screen.fill(black)
      camera.preview.alpha = 128
      #GPIO.wait_for_edge(17, GPIO.FALLING)
      shot = 0
      while shot < 2:
            #GPIO.output(GREEN_LED,True)
            for x in range (3, 0 , -1):
                 label = myfont.render(str(x),1,white)
                 screen.blit(label, labelPOS)
                 sleep(1)
                 pygame.display.flip()
                 screen.fill(black)
            #GPIO.output(GREEN_LED,False)
            sleep(1)
            pygame.display.flip()
            camera.capture('img{counter:02d}.jpg')
            shot += 1
            screen.fill(black)
      camera.stop_preview()
      pygame.display.quit()
      pygame.quit()

