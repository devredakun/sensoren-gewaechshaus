from gpiozero import DigitalInputDevice
from time import sleep

touch_pin = DigitalInputDevice(9)  # 21

try:
    while True:
        if touch_pin.value: 
            print("Finger berührt – Zugang genehmigt!")
            print("Tür macht auf !")
            sleep(3)
            print("Tür schließt wieder.")
        else:
            print("Keine Berührung – Tür bleibt zu")
        
        sleep(3)
except KeyboardInterrupt:
    print("Programm beendet")
