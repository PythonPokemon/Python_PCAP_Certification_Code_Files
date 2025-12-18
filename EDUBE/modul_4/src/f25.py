"""
Verarbeitung von Textdateien – readlines()
Dateien als Liste von Zeilen lesen

-----------------------------------------------------------
Was ist die Idee dahinter?
-----------------------------------------------------------
readlines() behandelt eine Textdatei **als Sammlung von Zeilen**
und liefert diese gesammelt als **Liste von Strings** zurück.

Jedes Listenelement entspricht genau **einer Zeile** der Datei.

-----------------------------------------------------------
Was macht readlines()?
-----------------------------------------------------------
• liest mehrere Zeilen auf einmal
• Rückgabewert: Liste von Strings
• jedes Element enthält i. d. R. ein \\n am Zeilenende
• wenn nichts mehr zu lesen ist → leere Liste []

Optional:
readlines(max_bytes)
→ liest höchstens max_bytes Zeichen auf einmal

-----------------------------------------------------------
Unterschied zu readline()
-----------------------------------------------------------
readline()  → liest GENAU EINE Zeile  
readlines() → liest MEHRERE Zeilen und gibt sie als Liste zurück  

Beide erkennen das Dateiende:
• readline()  → ""
• readlines() → []

-----------------------------------------------------------
Beispiel aus der Aufgabe
-----------------------------------------------------------
Wir:
1) lesen die Datei blockweise mit readlines()
2) nutzen einen Puffer (max. Bytes)
3) zählen Zeilen und Zeichen
4) geben den Dateiinhalt aus
"""

from os import strerror

try:
    zeichen_zaehler = 0                      # zählt alle Zeichen
    zeilen_zaehler = 0                       # zählt alle Zeilen

    stream = open("text.txt", "rt")          # Datei öffnen
    zeilen_liste = stream.readlines(20)      # max. 20 Bytes lesen

    while len(zeilen_liste) != 0:             # solange noch Daten da sind
        for zeile in zeilen_liste:            # jede Zeile im Block
            zeilen_zaehler += 1
            for zeichen in zeile:              # Zeichen der Zeile
                print(zeichen, end="")
                zeichen_zaehler += 1

        zeilen_liste = stream.readlines(10)   # nächsten Block lesen

    stream.close()                            # Stream schließen

    print("\n\nCharacters in file:", zeichen_zaehler)
    print("Lines in file:     ", zeilen_zaehler)

except IOError as fehler:
    print("I/O error occurred:", strerror(fehler.errno))



"""
-----------------------------------------------------------
Was passiert hier?
-----------------------------------------------------------
• readlines(20) liest so viele Zeilen, bis ~20 Bytes erreicht sind
• Rückgabe ist IMMER eine Liste
• äußere while-Schleife läuft blockweise
• innere Schleifen:
  - Zeilen zählen
  - Zeichen zählen
  - Inhalt ausgeben

-----------------------------------------------------------
⚠️ WICHTIG FÜR AUFGABEN / PRÜFUNG (EDUBE / PCAP)
-----------------------------------------------------------
• readlines() liefert eine LISTE
• Dateiende erkennt man an: []
• \\n zählt als Zeichen
• Puffergröße beeinflusst nur Performance, nicht Logik
• Sehr typische Prüfungsfrage:
  „Warum endet die while-Schleife?“
   → weil readlines() eine leere Liste zurückgibt

-----------------------------------------------------------
Typische Prüfungsfallen:
-----------------------------------------------------------
• readlines() mit read() verwechseln
• vergessen, neuen Block einzulesen
• leere Liste nicht als Abbruchbedingung erkennen
• annehmen, dass max_bytes = Anzahl Zeilen ist (FALSCH!)

-----------------------------------------------------------
Merke:
-----------------------------------------------------------
readlines() ist ideal für **blockweises,
zeilenorientiertes Lesen**, besonders bei
größeren Dateien.
"""
