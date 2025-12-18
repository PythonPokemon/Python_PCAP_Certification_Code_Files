"""
Verarbeitung von Textdateien – readline()
Zeilenweise Lesen statt Zeichenweise

-----------------------------------------------------------
Was ist die Idee dahinter?
-----------------------------------------------------------
Mit readline() wird eine Textdatei **zeilenweise** gelesen
anstatt als ein großer String oder als einzelne Zeichen.

Das ist sinnvoll, wenn:
• man mit Zeilen arbeiten möchte
• man Zeilen zählen will
• man große Dateien verarbeitet
• man Speicher sparen möchte

-----------------------------------------------------------
Was macht readline()?
-----------------------------------------------------------
• liest GENAU EINE Zeile aus der Datei
• Rückgabewert ist ein String (inkl. Zeilenumbruch \\n)
• wenn das Dateiende erreicht ist → Rückgabe: leerer String ""

→ leerer String = ABBRUCHBEDINGUNG

-----------------------------------------------------------
Beispiel aus der Aufgabe
-----------------------------------------------------------
Wir:
1) lesen die Datei zeilenweise
2) zählen die Zeilen
3) zählen alle Zeichen
4) geben den Inhalt aus
"""

from os import strerror

try:
    zeichen_zaehler = 0                      # zählt alle Zeichen
    zeilen_zaehler = 0                       # zählt alle Zeilen

    stream = open("text.txt", "rt")          # Datei öffnen
    zeile = stream.readline()                # erste Zeile lesen

    while zeile != "":                       # solange nicht Dateiende
        zeilen_zaehler += 1                  # neue Zeile erkannt
        for zeichen in zeile:                # Zeichen der Zeile
            print(zeichen, end="")            # ausgeben
            zeichen_zaehler += 1              # Zeichen zählen
        zeile = stream.readline()             # nächste Zeile lesen

    stream.close()                            # Stream schließen

    print("\n\nCharacters in file:", zeichen_zaehler)
    print("Lines in file:     ", zeilen_zaehler)

except IOError as fehler:
    print("I/O error occurred:", strerror(fehler.errno))



"""
-----------------------------------------------------------
Was passiert hier?
-----------------------------------------------------------
• readline() liest jeweils GENAU EINE Zeile
• leere Zeichenkette "" signalisiert Dateiende
• jede Zeile enthält meist ein \\n am Ende
• Zeichen- und Zeilenzähler laufen unabhängig

-----------------------------------------------------------
⚠️ WICHTIG FÜR AUFGABEN / PRÜFUNG (EDUBE / PCAP)
-----------------------------------------------------------
• readline() → eine Zeile pro Aufruf
• Dateiende erkennt man an: ""
• \\n zählt als Zeichen
• Sehr typische Prüfungsfrage:
  „Warum endet die while-Schleife?“
   → weil readline() "" zurückgibt

-----------------------------------------------------------
Typische Prüfungsfallen:
-----------------------------------------------------------
• readline() mit read() verwechseln
• vergessen, die nächste Zeile zu lesen
• Abbruchbedingung falsch formulieren
• close() vergessen

-----------------------------------------------------------
Merke:
-----------------------------------------------------------
readline() ist ideal für **kontrolliertes,
zeilenweises Lesen** und große Dateien.
"""
