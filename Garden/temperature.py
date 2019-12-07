#The ds18b20 sensor setup
# Wiring diagram https://thepihut.com/blogs/raspberry-pi-tutorials/ds18b20-one-wire-digital-temperature-sensor-and-the-raspberry-pi
# RPI Pin 1 to Red lead on thremometer
# RPI Pin 1 also to 4.7 resistor.  Resistor between Data lead (RPI Pin 7) and Yellow lead on thermometer
# RPI Pin 6 to Black lead on thrmometer

import os
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

temp_sensor = '/sys/bus/w1/devices/28-01142fd3c986/w1_slave'

def temp_raw():
    f = open(temp_sensor, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = temp_raw()
        
    temp_output = lines[1].find('t=')
    if temp_output != -1:
        temp_string = lines[1].strip() [temp_output+2:]
        temp_c = float(temp_string) / 1000
        temp_f = temp_c * 9 / 5 + 32
        return temp_c, temp_f
    
while True:
    print(read_temp())
    time.sleep(1)

