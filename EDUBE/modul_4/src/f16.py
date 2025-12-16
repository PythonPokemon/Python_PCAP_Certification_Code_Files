"""
Aktennamen & Streams – Text- vs. Binärmodus
Öffnen von Dateien mit open()

-----------------------------------------------------------
Text- vs. Binärströme – Grundidee
-----------------------------------------------------------
Python unterscheidet beim Arbeiten mit Dateien zwischen
**Textströmen** und **Binärströmen**.

Diese Unterscheidung ist extrem wichtig für:
• Portabilität (Windows / Linux / macOS)
• korrekte Verarbeitung von Zeilenumbrüchen
• korrekte Verarbeitung von Bytes (z. B. Bilder, PDFs)

-----------------------------------------------------------
Textmodus (Standard)
-----------------------------------------------------------
Ein Stream wird im **Textmodus** geöffnet, wenn:
• kein spezieller Modus angegeben wird
• oder der Modus kein "b" enthält

Eigenschaften:
• Daten werden als ZEICHEN (Strings) verarbeitet
• Zeilenumbrüche werden AUTOMATISCH angepasst

Plattform-Unterschiede:
• Unix/Linux:     \\n
• Windows:        \\r\\n

➡️ Python übersetzt diese Unterschiede AUTOMATISCH:
• Lesen:   \\r\\n → \\n
• Schreiben: \\n → \\r\\n (unter Windows)

⚠️ Dieser Vorgang ist für dein Programm VOLLSTÄNDIG TRANSPARENT.

-----------------------------------------------------------
Binärmodus
-----------------------------------------------------------
Ein Stream wird im **Binärmodus** geöffnet, wenn der Modus
ein "b" enthält (z. B. "rb", "wb").

Eigenschaften:
• Daten werden als BYTES verarbeitet
• KEINE Umwandlung von Zeilenumbrüchen
• KEINE automatische Kodierung

Wichtig für:
• Bilder
• Audiodateien
• Videos
• PDFs
• ZIP-Dateien
• jede Datei, die KEIN Text ist

-----------------------------------------------------------
Öffnen eines Streams mit open()
-----------------------------------------------------------
Syntax:
    stream = open(file, mode='r', encoding=None)

Parameter:
• file     → Dateiname (Pfad)
• mode     → Öffnungsmodus
• encoding → Zeichencodierung (nur im Textmodus sinnvoll)

Standardwerte:
• mode = "r"   (Lesen im Textmodus)
• encoding = plattformabhängig (meist UTF-8)

-----------------------------------------------------------
Beispiel: Textdatei öffnen (Standard)
-----------------------------------------------------------
"""
datei = open("textdatei.txt", "r")      # Textmodus (Standard)
inhalt = datei.read()                   # liest STRING
print(inhalt)
datei.close()



"""
-----------------------------------------------------------
Beispiel: Textdatei mit expliziter Kodierung
-----------------------------------------------------------
"""
datei = open("textdatei.txt", "r", encoding="utf-8")
inhalt = datei.read()
print(inhalt)
datei.close()



"""
-----------------------------------------------------------
Beispiel: Binärdatei öffnen
-----------------------------------------------------------
"""
datei = open("bild.png", "rb")           # Binärmodus
daten = datei.read()                     # liest BYTES
print(type(daten))                       # <class 'bytes'>
datei.close()



"""
-----------------------------------------------------------
⚠️ WICHTIG FÜR AUFGABEN / PRÜFUNG (EDUBE / PCAP)
-----------------------------------------------------------
• Textmodus:
  - arbeitet mit Strings
  - Zeilenumbrüche werden konvertiert
  - optional encoding angeben

• Binärmodus:
  - arbeitet mit Bytes
  - KEINE automatische Konvertierung
  - KEIN encoding erlaubt

• "b" im Modus → Binärdatei
• kein "b" → Textdatei

-----------------------------------------------------------
Typische Prüfungsfallen:
-----------------------------------------------------------
• Binärdatei im Textmodus öffnen → FEHLER
• encoding bei Binärdatei angeben → FEHLER
• Annahme, dass \\n überall gleich gespeichert wird → FALSCH
• Vergessen, dass open() standardmäßig Textmodus nutzt

-----------------------------------------------------------
Merke:
-----------------------------------------------------------
Textdatei → Zeichen + automatische Umwandlung  
Binärdatei → Bytes + KEINE Umwandlung  

Die Wahl des Modus entscheidet, wie Python
die Datei intern behandelt.
"""
