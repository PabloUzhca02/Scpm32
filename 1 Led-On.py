from machine import Pin
from time import sleep

L1 = Pin(19, Pin.OUT)

while True:
    L1.on()
    sleep(0.5)
    L1.off()
    sleep(0.5)
    
