import RPi.GPIO as gpio
from time import sleep

leds = [21, 20, 16, 12, 7, 8, 25, 24]

gpio.setmode(gpio.BCM)

for i in range(len(leds)):
    gpio.setup(leds[i], gpio.OUT)
    gpio.output(21,0)


for i in range(3):
    for j in range(len(leds)):
        gpio.output(leds[j],1)
        sleep(0.2)
        gpio.output(leds[j],0)
gpio.cleanup(),