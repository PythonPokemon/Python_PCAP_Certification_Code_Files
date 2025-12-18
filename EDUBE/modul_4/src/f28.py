"""
Verarbeitung von Textdateien – write(): Fortsetzung
Zeilenweise Schreiben & stderr-Ausgabe

-----------------------------------------------------------
Was ist neu in diesem Beispiel?
-----------------------------------------------------------
Im Gegensatz zum vorherigen Beispiel:
• schreiben wir **GANZE ZEILEN auf einmal**
• kein Schreiben Zeichen für Zeichen mehr
• das Ergebnis in der Datei ist IDENTISCH

Das zeigt:
→ write() kann **Strings jeder Länge** schreiben
→ Zeichenweises Schreiben ist möglich, aber unnötig

-----------------------------------------------------------
Erinnerung: write()
-----------------------------------------------------------
• write() schreibt exakt den übergebenen String
• KEIN automatischer Zeilenumbruch
• \n muss explizit ergänzt werden
• Datei muss im Schreibmodus geöffnet sein

-----------------------------------------------------------
Beispiel aus der Aufgabe
-----------------------------------------------------------
Wir:
1) erzeugen eine neue Datei newtext.txt
2) schreiben 10 Zeilen hinein
3) jede Zeile wird mit EINEM write()-Aufruf geschrieben
"""

from os import strerror

try:
    datei = open("newtext.txt", "wt")          # Datei im Schreibmodus öffnen

    for nummer in range(10):                   # 10 Zeilen erzeugen
        datei.write("line #" + str(nummer + 1) + "\n")

    datei.close()                              # Datei schließen

except IOError as fehler:
    print("I/O error occurred:", strerror(fehler.errno))



"""
-----------------------------------------------------------
Inhalt der Datei newtext.txt
-----------------------------------------------------------
line #1
line #2
line #3
line #4
line #5
line #6
line #7
line #8
line #9
line #10

-----------------------------------------------------------
Was passiert hier?
-----------------------------------------------------------
• write() bekommt direkt den vollständigen Zeilen-String
• \n erzeugt den Zeilenumbruch
• weniger Code, gleiche Wirkung wie vorher

-----------------------------------------------------------
stderr – Fehlerausgabe
-----------------------------------------------------------
Neben Dateien kann write() auch auf **Standard-Fehlerausgabe**
angewendet werden.

⚠️ WICHTIG:
• stderr ist IMMER offen
• NICHT mit open() öffnen!
• nur schreiben

Beispiel:
"""

import sys
sys.stderr.write("Error message")



"""
-----------------------------------------------------------
⚠️ WICHTIG FÜR AUFGABEN / PRÜFUNG (EDUBE / PCAP)
-----------------------------------------------------------
• write() schreibt exakt den übergebenen String
• \n muss IMMER manuell ergänzt werden
• "wt" überschreibt vorhandene Dateien
• stderr wird NICHT geöffnet – nur benutzt

-----------------------------------------------------------
Typische Prüfungsfallen:
-----------------------------------------------------------
• Datei im falschen Modus geöffnet
• fehlender Zeilenumbruch
• Versuch, stderr mit open() zu öffnen

-----------------------------------------------------------
Merke:
-----------------------------------------------------------
write() kann:
• einzelne Zeichen
• ganze Strings
• ganze Zeilen

→ Zeilenweise schreiben ist der saubere Standard.
"""
