import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)

gpio.setup(15, gpio.IN)

gpio.setup(14, gpio.OUT)

while True:
    gpio.output(14, gpio.input(15))
    sleep(0.1)
    