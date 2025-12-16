"""
Dateiströme (File Streams)
Lesen, Schreiben und die aktuelle Dateiposition

-----------------------------------------------------------
Was ist ein Dateistream?
-----------------------------------------------------------
Ein Dateistream ist eine **Verbindung zwischen Programm und Datei**.
Über diesen Strom werden Daten:
• aus einer Datei GELESEN
• in eine Datei GESCHRIEBEN

Das Öffnen eines Streams bestimmt,
WAS erlaubt ist und WAS NICHT.

-----------------------------------------------------------
Öffnungsmodi (Open Modes)
-----------------------------------------------------------
Beim Öffnen einer Datei MUSS ein Modus angegeben werden.

Die drei grundlegenden Modi sind:

• Lesemodus      → nur lesen
• Schreibmodus   → nur schreiben
• Update-Modus   → lesen UND schreiben

Wenn ein Stream im falschen Modus verwendet wird,
wirft Python eine Ausnahme.

-----------------------------------------------------------
Modi im Überblick
-----------------------------------------------------------
"r"   → read      (lesen)
"w"   → write     (schreiben, Datei wird neu erstellt/geleert)
"r+"  → read+write (lesen & schreiben)
"w+"  → write+read (neu erstellen & lesen/schreiben)

⚠️ Wichtig:
Nicht erlaubte Operationen führen zu einer Exception
(UnsupportedOperation).

-----------------------------------------------------------
Die Analogie: Tonbandgerät
-----------------------------------------------------------
Ein Dateistream verhält sich wie ein Tonband:

• Lesen  → der Kopf wandert nach vorne
• Schreiben → der Kopf wandert nach vorne und überschreibt/ergänzt
• Python merkt sich die **aktuelle Dateiposition**

Diese Position nennt man:
→ aktuelle Dateiposition (file pointer)

-----------------------------------------------------------
Beispiel: Lesen aus einer Datei
-----------------------------------------------------------
"""
datei = open("beispiel.txt", "r")      # Datei im Lesemodus öffnen
inhalt = datei.read()                  # gesamten Inhalt lesen
print(inhalt)                          # Ausgabe des Dateiinhalts
datei.close()                          # Stream schließen



"""
-----------------------------------------------------------
Beispiel: Schreiben in eine Datei
-----------------------------------------------------------
"""
datei = open("beispiel.txt", "w")      # Datei im Schreibmodus öffnen
datei.write("Hallo Datei!\n")          # Text in die Datei schreiben
datei.write("Zweite Zeile\n")
datei.close()                          # Stream schließen



"""
-----------------------------------------------------------
Beispiel: Lesen UND Schreiben (Update-Modus)
-----------------------------------------------------------
"""
datei = open("beispiel.txt", "r+")     # Lesen und Schreiben erlaubt
print(datei.read())                    # zuerst lesen
datei.write("Neue Zeile am Ende\n")    # dann schreiben
datei.close()



"""
-----------------------------------------------------------
⚠️ WICHTIG FÜR AUFGABEN / PRÜFUNG (EDUBE / PCAP)
-----------------------------------------------------------
• Der Öffnungsmodus bestimmt ALLE erlaubten Operationen
• Lesen im Schreibmodus → Fehler
• Schreiben im Lesemodus → Fehler
• Jeder Lese-/Schreibvorgang verändert die Dateiposition
• Dateien sollten IMMER geschlossen werden

-----------------------------------------------------------
Typische Prüfungsfallen:
-----------------------------------------------------------
• Datei vergessen zu schließen
• Falscher Modus gewählt
• Annahme, dass Lesen die Position nicht verändert
• Datei wird mit "w" geöffnet → Inhalt wird GELÖSCHT

-----------------------------------------------------------
Merke:
-----------------------------------------------------------
Ein Dateistream ist zustandsbehaftet:
Was du liest oder schreibst, beeinflusst,
wo der nächste Zugriff beginnt.
"""
