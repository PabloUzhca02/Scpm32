import network
import espnow
from machine import Pin, SoftI2C #Configuracion de hardware
from lcd_api import LcdApi #Configuracion de la pantalla LCD
from i2c_lcd import I2cLcd #Configuracion de la pantalla LCD
from time import sleep #Importamos la configuracion de tiempo


I2C_ADDR = 0x27 #Direccion I2C de la pantalla
totalRows = 2 #Numero de filas en la pantalla
totalColums = 16 #Numero de columnas en la pantalla

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)
lcd = I2cLcd (i2c, I2C_ADDR, totalRows, totalColums)

B1 = Pin(19, Pin.IN, Pin.PULL_UP)


sta = network.WLAN(network.STA_IF)
sta.active(True)



lcd.move_to(0,0)
lcd.putstr("ESP-NOW Emisor 1")


e = espnow.ESPNow()
e.active(True)


mac = b'@"\xd8^\xe8\x18'
e.add_peer(mac)

while True:
    if B1.value()==0:
        e.send(mac, "4 Jhonatan Malla")
        e.send(mac, "4 blanco")
        lcd.move_to(0,1)
        lcd.putstr(" Enviando msg  ")
        sleep(1)
        lcd.move_to(0,1)
        lcd.putstr("               ")
        
