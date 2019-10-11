from picamera import PiCamera
from time import sleep
import time

camera = PiCamera()
imgnum = 0

while True:
    file1 = "image{0:04d}.jpg".format(imgnum)
    path = "/home/pi/Pictures/timelapse/" + file1
    camera.capture(path)
    imgnum += 1
    sleep(14400)
    
#Stitch code
# avconv -r 10 -i image%04d.jpg -r 10 -vcodec libx264 -crf 20 -g 15 timelapse.mp4

#player code
# omxplayer timelapse.mp4 -o hdmi
