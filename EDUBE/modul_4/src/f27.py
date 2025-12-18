"""
Verarbeitung von Textdateien – write()
Schreiben von Textdateien in Python

-----------------------------------------------------------
Was macht write()?
-----------------------------------------------------------
Die Methode write() schreibt **Textdaten** in eine Datei.

Wichtig:
• write() erwartet **genau einen String**
• write() fügt **KEINEN Zeilenumbruch automatisch hinzu**
• Zeilenumbrüche (\n) müssen explizit ergänzt werden
• Die Datei MUSS im Schreibmodus geöffnet sein

-----------------------------------------------------------
Syntax
-----------------------------------------------------------
datei.write(text)

-----------------------------------------------------------
Wichtige Open-Modi
-----------------------------------------------------------
"wt"  → write text  
• erstellt die Datei neu  
• überschreibt den Inhalt, falls die Datei existiert  

-----------------------------------------------------------
Beispiel aus der Aufgabe
-----------------------------------------------------------
Wir:
1) erzeugen eine neue Textdatei (newtext.txt)
2) schreiben 10 Zeilen hinein
3) schreiben absichtlich Zeichen für Zeichen,
   um zu zeigen, dass write() auch mit einzelnen
   Zeichen funktioniert
"""

from os import strerror

try:
    datei = open("newtext.txt", "wt")             # Datei im Schreibmodus öffnen

    for nummer in range(10):                      # 10 Zeilen erzeugen
        zeile = "line #" + str(nummer + 1) + "\n" # Text + Zeilenumbruch

        for zeichen in zeile:                     # Zeichenweise schreiben
            datei.write(zeichen)

    datei.close()                                 # Datei schließen

except IOError as fehler:
    print("I/O error occurred:", strerror(fehler.errno))



"""
-----------------------------------------------------------
Was steht danach in der Datei?
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
• open("newtext.txt", "wt")
  → erstellt eine neue Datei (oder überschreibt sie)
• write() schreibt exakt den übergebenen String
• \n sorgt für den Zeilenumbruch
• Schreiben Zeichen für Zeichen ist erlaubt,
  aber NICHT notwendig

-----------------------------------------------------------
⚠️ WICHTIG FÜR AUFGABEN / PRÜFUNG (EDUBE / PCAP)
-----------------------------------------------------------
• write() schreibt **KEINEN** automatischen Zeilenumbruch
• \n muss IMMER selbst ergänzt werden
• Schreiben im Lesemodus ("r") führt zu einer Exception
• Datei im Schreibmodus überschreibt bestehende Inhalte

-----------------------------------------------------------
Typische Prüfungsfallen:
-----------------------------------------------------------
• vergessenes \n → alles landet in einer Zeile
• write() mit Zahlen → FEHLER (write() braucht String!)
• Datei nicht schließen → Daten evtl. nicht vollständig geschrieben

-----------------------------------------------------------
Merke:
-----------------------------------------------------------
write() ist einfach, direkt und präzise:
• String rein → exakt dieser Text geht in die Datei
• Keine Magie, keine Automatismen
"""
