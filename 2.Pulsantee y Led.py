from machine import Pin
import time

# Configuración del botón y el LED
boton = Pin(15, Pin.IN, Pin.PULL_UP)  # Pin 15 como entrada con resistencia pull-up
led = Pin(2, Pin.OUT)                # Pin 2 como salida para el LED

while True:
    if not boton.value():  # Si el botón se presiona (valor es 0)
        led.on()           # Encender LED
    else:
        led.off()          # Apagar LED
    time.sleep(0.1)        # Pequeña pausa para evitar rebotes
