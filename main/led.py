from machine import Pin
from time import sleep

class Led:
    def blink(self):
        led = Pin(2, Pin.OUT)
        while True:
            led.on()
            sleep(1)
            led.off()
            sleep(1)
