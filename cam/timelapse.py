from picamera import PiCamera
from time import sleep
import time
import datetime
import os

camera = PiCamera()
imgnum = 0
imageloc = "/home/pi/Pictures/timelapse/"

foldername = datetime.datetime.now()
newname = foldername.strftime("%f")

sourceloc = imageloc + newname

os.makedirs(sourceloc)

while True:
    camera.rotation = 90
    file1 = "image{0:04d}.jpg".format(imgnum)
    path = sourceloc + "/" + file1
    camera.capture(path)
    imgnum += 1
    sleep(300)
    
#Stitch code
# avconv -r 10 -i image%04d.jpg -r 10 -vcodec libx264 -crf 20 -g 15 timelapse.mp4

#player code
# omxplayer timelapse.mp4 -o hdmi

#Stitch application
# sudo apt-get install libav-tools

