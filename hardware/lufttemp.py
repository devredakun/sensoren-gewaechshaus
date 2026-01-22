import time
import board
import adafruit_dht

dht = adafruit_dht.DHT11(board.D11)

try:
    while True:
        try:
            temp = dht.temperature
            hum = dht.humidity
            print(f"Temperatur: {temp:.1f} °C")
            print(f"Luftfeuchtigkeit: {hum:.1f} %")
        except RuntimeError as e:
            print("Lesefehler:", e)
        time.sleep(5)
finally:
    dht.exit()

