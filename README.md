# LF12 – Projekt: Sensoren Gewächshaus  
IT – 3. Lehrjahr

**WICHTIG**: Dieses Projekt ist rein IT-technisch und dient ausschließlich schulischen Zwecken.  
Es enthält **KEINE** Anleitung zum Anbau von Pflanzen jeglicher Art.

### Projektkontext
Im Rahmen des CanG (Cannabisgesetz) vom 1. April 2024 wurde der private und vereinsmäßige Umgang mit Cannabis unter strengen Auflagen legalisiert.  
Dieses Projekt betrachtet ausschließlich die technische Umsetzung eines Überwachungssystems für ein hypothetisches Gewächshaus (ca. 100 Plätze).

### Geforderte Inhalte (werden vollständig bearbeitet)
- Bauliche/technische Rahmenbedingungen  
- Sicherheitsanforderungen  
- Dokumentation, Nachverfolgbarkeit & IT  
- 5 Sensorarten (auf Raspberry Pi umgesetzt)  
- Infrastruktur-Zustände und Aktoren  
- Netzwerkarchitektur
- Hardware-Konkretisierung (Redundanz, Datenspeicherung, Sicherheit)  
- Realisierung mit Python und Raspberry Pi  
- Übersichtsschaltplan + Quellcode + PDF-Abgabe

### Verwendete Sensorarten (generisch, keine konkreten Modelle)
1. Lufttemperatur- und Luftfeuchtigkeitssensor  
2. Bodenfeuchtigkeitssensor (kapazitiv)  
3. Lichtintensitätssensor  
4. EC-Sensor (Leitfähigkeit der Nährlösung)  
5. CO₂-Sensor  

### Repo-Struktur
- `/docs`      → Schaltpläne, Fotos der Verdrahtung, finaler Projektbericht (PDF)  
- `/hardware`  → Beschreibung der bereitgestellten Komponenten (nur Typen, keine Seriennummern)  
- `/src`       → Python-Code (ein Sensor pro Datei + Hauptprogramm)  
- `/data`      → CSV-Datei mit Messwerten  

### Rechtlicher Hinweis / Legal Disclaimer
Dieses Projekt wurde ausschließlich im Rahmen des Unterrichts an einer staatlich anerkannten Berufsbildenden Schule in Deutschland erstellt (§ 3 CanG, § 34d BtMG in der aktuellen Fassung).  
Es dient rein didaktischen Zwecken und stellt keine Anleitung zum Anbau, zur Verarbeitung oder zum Vertrieb von Betäubungsmitteln dar.  
Das gesamte Repository und alle enthaltenen Materialien sind urheberrechtlich geschützt (© 2025 [Dein Name]).  
Jede Form der Reproduktion, Weitergabe oder Nutzung außerhalb des schulischen Rahmens ist untersagt.

Projekt von: ZSRe & Lami
Betreuung: Grok (KI-Mentor)
Stand: November 2025
