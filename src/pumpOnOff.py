import os
import RPi.GPIO as GPIO             #Importamos a biblioteca GPIO
import time                         #Importamos time (time.sleep)
GPIO.setmode(GPIO.BCM)              #Colocamos a placa em modo BCM
GPIO_RELAY = 12                     #Usamos o pin GPIO 12 para acionar o módulo relê
GPIO.setwarnings(False)             #Desabilitando warnings
GPIO.setup(GPIO_RELAY,GPIO.OUT)     #Configuramos RELAY como saida

GPIO.output(GPIO_RELAY, GPIO.LOW)
time.sleep(5)                       #Tempo que a planta será regada

GPIO.output(GPIO_RELAY, GPIO.HIGH)

GPIO.cleanup();
