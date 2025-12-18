"""
Verarbeitung von Textdateien – Dateiobjekt als Iterator
Iterieren über Dateien mit for-Schleifen

-----------------------------------------------------------
Was ist die Idee dahinter?
-----------------------------------------------------------
Ein Dateiobjekt, das mit open() im Textmodus erzeugt wird,
ist **iterierbar**.

Das bedeutet:
• Die Datei kann direkt in einer for-Schleife verwendet werden
• Jede Iteration liefert automatisch die **nächste Zeile**
• Python nutzt intern das Iterator-Protokoll (__iter__ / __next__)

-----------------------------------------------------------
Warum ist das wichtig?
-----------------------------------------------------------
• extrem kompakter Code
• keine expliziten Aufrufe von:
  - readline()
  - readlines()
• kein manuelles EOF-Handling nötig
• Datei wird **automatisch geschlossen**, wenn das Ende erreicht ist

-----------------------------------------------------------
Wie funktioniert das intern?
-----------------------------------------------------------
• open(...) liefert ein Dateiobjekt
• das Dateiobjekt ist iterierbar
• __next__() gibt jeweils die nächste Zeile zurück
• beim Dateiende wird StopIteration ausgelöst
• Python schließt die Datei automatisch

-----------------------------------------------------------
Beispiel aus der Aufgabe
-----------------------------------------------------------
Wir:
1) iterieren direkt über die Datei
2) zählen Zeilen und Zeichen
3) geben den Dateiinhalt aus
"""

from os import strerror

try:
    zeichen_zaehler = 0                          # zählt alle Zeichen
    zeilen_zaehler = 0                           # zählt alle Zeilen

    for zeile in open("text.txt", "rt"):          # Datei DIREKT iterieren
        zeilen_zaehler += 1
        for zeichen in zeile:                     # Zeichen der Zeile
            print(zeichen, end="")
            zeichen_zaehler += 1

    print("\n\nCharacters in file:", zeichen_zaehler)
    print("Lines in file:     ", zeilen_zaehler)

except IOError as fehler:
    print("I/O error occurred:", strerror(fehler.errno))



"""
-----------------------------------------------------------
Was passiert hier?
-----------------------------------------------------------
• open("text.txt", "rt") erzeugt ein iterierbares Dateiobjekt
• for zeile in open(...):
  → jede Iteration liefert eine komplette Zeile
• keine explizite close()-Anweisung nötig
• Datei wird automatisch geschlossen, wenn EOF erreicht ist

-----------------------------------------------------------
⚠️ WICHTIG FÜR AUFGABEN / PRÜFUNG (EDUBE / PCAP)
-----------------------------------------------------------
• Dateiobjekte sind ITERIERBAR
• for zeile in open(...):
  → ist die empfohlene, pythonische Lösung
• Keine read(), readline() oder readlines() nötig
• Datei schließt sich automatisch am Ende der Iteration

-----------------------------------------------------------
Typische Prüfungsfallen:
-----------------------------------------------------------
• glauben, dass open() nur „liest“, aber nicht iterierbar ist
• close() manuell aufrufen wollen (hier nicht nötig)
• annehmen, dass zeile einzelne Zeichen enthält (FALSCH!)
  → zeile ist IMMER ein kompletter String (eine Zeile)

-----------------------------------------------------------
Merke:
-----------------------------------------------------------
Die for-Schleife über ein Dateiobjekt ist:
• die sauberste
• die sicherste
• die pythonischste Art,
Textdateien zeilenweise zu lesen.
"""
