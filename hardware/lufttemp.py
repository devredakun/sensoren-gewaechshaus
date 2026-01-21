import random
from time import sleep

try:
    while True:
        # Werte für Gewächshaus
        temp = round(random.uniform(18.0, 30.0), 1)      # 18–30 °C
        feuchte = round(random.uniform(35.0, 75.0), 1)   # 35–75 %

        print(f"Temperatur: {temp} °C")
        print(f"Luftfeuchtigkeit: {feuchte} %")

        # Einfache Aktor-Simulation
        if temp > 28:
            print("Zu heiß → Fenster öffnen oder Klimaanlage einschalten!")
        elif temp < 20:
            print("Zu kalt → Heizung einschalten!")
        else:
            print("Temperatur ok – keine Aktion nötig")

        print("---")
        sleep(5)
except KeyboardInterrupt:
    print("Programm beendet")
