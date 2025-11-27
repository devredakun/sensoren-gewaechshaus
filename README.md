# LF12 – Projekt: Sensoren Gewächshaus (IT – 3. Lehrjahr)

**Ziel des Projekts**  
Erstellung eines reinen IT-Systems zur Überwachung und Steuerung eines Gewächshauses (ca. 100 Plätze) im Kontext der Cannabis-Legalisierung (Stand: November 2025).  
**WICHTIG**: Dieses Projekt enthält KEINE Anleitung zum Anbau von Pflanzen – es geht ausschließlich um Hard- und Software!

**Rechtlicher Kontext**  
Seit 1. April 2024 ist der Eigenanbau und der Betrieb von Cannabis-Clubs in Deutschland unter Auflagen erlaubt. In Sachsen gibt es aktuell ca. 23 zugelassene Clubs.

### Geforderte Inhalte (werden alle abgearbeitet)
- Bauliche / technische Rahmenbedingungen (konzeptionell)  
- Sicherheitsanforderungen  
- Dokumentation, Nachverfolgbarkeit & IT  
- 5 Sensorarten (real auf Raspberry Pi)  
- Infrastruktur-Zustände & Aktoren  
- Netzwerkarchitektur, MQTT-Broker, InfluxDB, Node-RED, Home-Assistant  
- Hardware-Konkretisierung (Netzabdeckung, Datenspeicherung, Redundanz, Sicherheit)  
- Realisierung mit Python-Skripten und echtem Raspberry Pi  
- Übersichtsschaltplan + Quellcode + PDF-Abgabe

### Verwendete 5 Sensoren (genaue Auswahl)
1. Lufttemperatur + Luftfeuchtigkeit → DHT22  
2. Bodenfeuchtigkeit → kapazitiver Sensor (analog)  
3. Lichtintensität → BH1750  
4. EC-Wert (Electrical Conductivity) → analoger EC-Sensor  
5. CO2-Konzentration → MH-Z19B  

### Aktoren (zur Regelung)
- 4-Kanal-Relaismodul (für Pumpe, Lüfter, LED-Beleuchtung)

### Repo-Struktur
