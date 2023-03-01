import RPi.GPIO as gpio
from time import sleep

dac = [26, 19, 13, 6, 5, 11, 9, 10]

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

def read():
    global num
    num = [0,0,0,0,0,0,0,0]
    arr = list(bin(int(input())))[2:10:]
    for i in range(len(arr)):
        num[len(arr)-1-i] = int(arr[i])
    print(num, arr)

for i in range(100):
    read()
    gpio.output(dac[::-1], num)
    sleep(1)
    print('continue')

gpio.output(dac, [0,0,0,0,0,0,0,0])
gpio.cleanup(),