from gpiozero import DigitalInputDevice
from time import sleep

boden_pin = DigitalInputDevice(27)  # GPIO 27 - 13

print("Drücke Ctrl+C zum Beenden")

try:
    while True:
        if boden_pin.value:
            print("Der Boden ist trocken")
        else:
            print("Der Boden ist feucht")
        sleep(1) 
except KeyboardInterrupt:
    print("Programm beendet")