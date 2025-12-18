"""
Bytearrays – Fortsetzung
Arbeiten mit Bytearrays wie mit Listen

-----------------------------------------------------------
Was ist wichtig bei bytearray?
-----------------------------------------------------------
Ein bytearray verhält sich in vielen Punkten wie eine Liste:

• veränderbar (mutable)
• len() funktioniert
• Indexzugriff möglich
• iteration mit for

ABER: es gibt strenge Regeln für die Werte!

-----------------------------------------------------------
⚠️ WICHTIGE EINSCHRÄNKUNGEN
-----------------------------------------------------------
Jedes Element eines bytearray muss sein:
• ein Integer
• im Wertebereich 0 bis 255 (inklusive)

❌ data[0] = "A"        → TypeError
❌ data[0] = 300        → ValueError
✔️ data[0] = 65         → OK

-----------------------------------------------------------
Beispiel aus der Aufgabe
-----------------------------------------------------------
Wir erzeugen ein bytearray mit 10 Bytes
und füllen es mit absteigenden Werten.
"""

data = bytearray(10)                 # 10 Bytes, alle initial 0

for i in range(len(data)):            # Index-basierte Iteration
    data[i] = 10 - i                  # Werte: 10,9,8,...,1

# Ausgabe der Bytes als Hex-Werte
for b in data:
    print(hex(b))



"""
-----------------------------------------------------------
Was passiert hier?
-----------------------------------------------------------
• bytearray(10)
  → erzeugt 10 Bytes Speicher

• data[i] = 10 - i
  → jeder Index bekommt einen Integer (0–255 erlaubt)

• hex(b)
  → zeigt den Byte-Wert in hexadezimaler Darstellung
    (typisch für Binärdaten!)

Ausgabe:
0xa
0x9
0x8
0x7
0x6
0x5
0x4
0x3
0x2
0x1

-----------------------------------------------------------
Warum hex()?
-----------------------------------------------------------
• Binärdaten werden oft hexadezimal dargestellt
• kompakter als Dezimalzahlen
• Standard in Low-Level- und Datei-Analyse

-----------------------------------------------------------
⚠️ WICHTIG FÜR AUFGABEN / PRÜFUNG (EDUBE / PCAP)
-----------------------------------------------------------
• bytearray speichert rohe Bytes (0–255)
• Jedes Element ist ein Integer
• bytearray ist veränderbar
• Ideal für Binärdateien (rb / wb)

-----------------------------------------------------------
Typische Prüfungsfallen:
-----------------------------------------------------------
• falscher Wertebereich (>255)
• Zuweisung von Strings statt Integern
• Verwechslung von bytearray und bytes

-----------------------------------------------------------
Merke:
-----------------------------------------------------------
bytearray = Liste aus Bytes
→ perfekt für Binärdateien und Low-Level-Daten.
"""
