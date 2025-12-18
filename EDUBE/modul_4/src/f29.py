"""
Was ist ein bytearray?
Binärdaten (amorphe Daten) in Python speichern

-----------------------------------------------------------
Was ist das Problem?
-----------------------------------------------------------
Nicht alle Daten haben eine klare Struktur wie:
• Text (Strings)
• Zahlen
• Listen mit Elementen

Manche Daten bestehen **nur aus rohen Bytes**:
• Bilder (z. B. Bitmap)
• Audio-Dateien
• Binärdateien
• Netzwerkdaten

Diese nennt man **amorphe Daten**:
→ keine erkennbare Form
→ Bedeutung ist dem Code oft egal oder unbekannt

Solche Daten lassen sich NICHT sinnvoll speichern als:
• str
• list
• tuple

-----------------------------------------------------------
Lösung: bytearray
-----------------------------------------------------------
Python stellt dafür eine spezielle Klasse bereit:
    bytearray

Ein bytearray ist:
• ein veränderbares Array aus Bytes
• jedes Element liegt im Bereich 0–255
• ideal für Binärdateien

-----------------------------------------------------------
Grundlegende Erzeugung
-----------------------------------------------------------
Wir erzeugen ein bytearray mit fester Länge.
Alle Bytes werden automatisch mit 0 gefüllt.
"""

daten = bytearray(10)              # bytearray mit 10 Bytes erzeugen
print(daten)



"""
Ausgabe:
bytearray(b'\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00')

-----------------------------------------------------------
Was bedeutet das?
-----------------------------------------------------------
• \\x00 ist die hexadezimale Darstellung von 0
• jedes Element ist ein einzelnes Byte
• insgesamt 10 Bytes Speicher

-----------------------------------------------------------
Zugriff auf einzelne Bytes
-----------------------------------------------------------
bytearray verhält sich ähnlich wie eine Liste.
"""

daten[0] = 65                       # ASCII-Code für 'A'
daten[1] = 66                       # ASCII-Code für 'B'
daten[2] = 255                      # maximaler Byte-Wert

print(daten)
print(daten[0], daten[1], daten[2])



"""
-----------------------------------------------------------
⚠️ WICHTIG FÜR AUFGABEN / PRÜFUNG (EDUBE / PCAP)
-----------------------------------------------------------
• bytearray speichert **rohe Binärdaten**
• Wertebereich pro Element: 0–255
• bytearray ist VERÄNDERBAR (im Gegensatz zu bytes)
• Standardinitialisierung erfolgt mit 0

-----------------------------------------------------------
Typische Prüfungsfallen:
-----------------------------------------------------------
• Verwechslung von bytes und bytearray
• Versuch, Strings direkt als Binärdaten zu nutzen
• Annahme, dass bytearray Zeichen speichert (es speichert BYTES!)

-----------------------------------------------------------
Merke:
-----------------------------------------------------------
Wenn du mit Binärdateien arbeitest (rb / wb):
→ bytearray ist das richtige Werkzeug.
"""
