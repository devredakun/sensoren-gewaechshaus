# src/04_co2_sensor.py
# LF12-Projekt: CO2/Luftqualitätssensor (MQ-2, digital Ausgang)
# Rein IT-Überwachung – KEINE Anleitung zum Anbau von Pflanzen!

from gpiozero import DigitalInputDevice
from time import sleep

# Konfiguration: GPIO-Pin (BCM-Nummer)
mq2_pin = DigitalInputDevice(22)  # GPIO 22 – passe an, wenn du einen anderen Pin verwendet hast

print("MQ-2 CO2/Luftqualitätssensor gestartet")
print("Ausgabe: Normal oder Hoch (Gas/Rauch erkannt)")
print("Drücke Ctrl+C zum Beenden")

try:
    while True:
        if mq2_pin.value == 0:  # LOW = Gas/Rauch erkannt (typische Logik bei MQ-2 Modulen)
            print("CO2/Luftqualität: Hoch – Achtung, Gas/Rauch erkannt!")
        else:
            print("CO2/Luftqualität: Normal")
        sleep(1)  # 1 Sekunde warten
except KeyboardInterrupt:
    print("Programm beendet")