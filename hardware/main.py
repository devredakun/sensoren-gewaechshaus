from time import sleep
from datetime import datetime
import csv

DATA_FILE = "../data/messwerte.csv"

try:
    with open(DATA_FILE, 'x', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Zeit", "Sensor-Ausgaben", "Aktoren"])
except FileExistsError:
    pass

try:
    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n=== Messung um {now} ===")

        aktoren = []

        # 1. Lichtsensor
        print("\nLichtsensor:")
        exec(open("lichtsensor.py").read())

        # 2. Bodenfeuchtigkeit
        print("\nBodenfeuchtigkeit:")
        exec(open("feuchtigkeit.py").read())  # z.B. "Der Boden ist feucht" oder "trocken"
        if "trocken" in open("feuchtigkeit.py").read().lower():
            aktoren.append("Zu trocken → Sprinkler/Pumpe für 30 Minuten an!")

        # 3. CO2 (cozwei.py)
        print("\nCO2-Sensor:")
        exec(open("cozwei.py").read())  
        if "hoch" in open("cozwei.py").read().lower():
            aktoren.append("CO2/Luftqualität hoch → Lüfter an!")

        # 4. Lufttemp/Feuchte
        print("\nLuft-Temperatur/Feuchte:")
        exec(open("lufttemp.py").read()) 
       
        luft_content = open("lufttemp.py").read()
        if any(str(t) in luft_content for t in range(29, 35)):
            aktoren.append("Zu heiß → Fenster öffnen oder Klimaanlage einschalten!")
        if any(str(t) in luft_content for t in range(10, 20)):
            aktoren.append("Zu kalt → Heizung einschalten!")

        # 5. Finger/Touch-Sensor
        print("\nFinger-Sensor:")
        exec(open("fingersensor.py").read()) 
        if "berührt" in open("fingersensor.py").read().lower():
            aktoren.append("Finger berührt – Zugang genehmigt!")
            aktoren.append("Tür macht auf für 5 Sekunden!")
            sleep(5) 
            aktoren.append("Tür schließt wieder.")

        # Aktoren-Ausgabe
        if aktoren:
            print("\nAktoren-Simulation:")
            for a in aktoren:
                print(f"  - {a}")
        else:
            print("\nKeine Aktion nötig")

        # CSV-Log (einfach – füge mehr Details hinzu, wenn du willst)
        with open(DATA_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([now, "Sensoren ausgeführt", "; ".join(aktoren)])

        print("=" * 60)
        sleep(30)
except KeyboardInterrupt:
    print("System beendet")
