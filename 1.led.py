import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)

gpio.setup(14, gpio.OUT)
gpio.output(14,0)

for i in range(4):
    sleep(1)
    gpio.output(14,0)
    sleep(1)
    gpio.output(14,1)
gpio.output(14,0)
    

