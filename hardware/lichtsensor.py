from gpiozero import DigitalInputDevice
from time import sleep

lichtsensor = DigitalInputDevice(6)  # 31

try:
    while True:
        if lichtsensor.value:
            print("Es ist dunkel")
        else:
            print("Es werde Licht")
        sleep(1)

except KeyboardInterrupt:
    print("Programm beendet")
