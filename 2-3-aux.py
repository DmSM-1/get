import RPi.GPIO as gpio
from time import sleep

leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3,  2]
buffer = [0,0,0,0,0,0,0,0]

gpio.setmode(gpio.BCM)
gpio.setup(leds, gpio.OUT)
gpio.setup(aux, gpio.IN)
gpio.output(leds,[0,0,0,0,0,0,0,0])

for i in range(900):
    for i in range(len(buffer)):
        buffer = gpio.input(aux)
    gpio.output(leds, buffer)
    sleep(0.1)
gpio.cleanup(),