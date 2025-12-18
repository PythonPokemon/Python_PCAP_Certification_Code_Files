"""
Verarbeitung von Textdateien – Fortsetzung
Gesamte Datei mit read() lesen und Zeichen zählen

-----------------------------------------------------------
Was ist die Idee dahinter?
-----------------------------------------------------------
Wenn man **sicher ist**, dass eine Datei:
• nicht zu groß ist
• problemlos komplett in den Speicher passt

kann man den **gesamten Inhalt auf einmal** mit read() einlesen.

⚠️ Achtung:
Sehr große Dateien (z. B. mehrere GB) dürfen NICHT so gelesen werden,
da sonst Speicherprobleme oder Systemabstürze drohen.

-----------------------------------------------------------
Wichtige Eigenschaft von read()
-----------------------------------------------------------
• read() ohne Argumente liest die **komplette Datei**
• Rückgabewert ist **ein String**
• Jeder Buchstabe, jedes Leerzeichen und jeder Zeilenumbruch
  ist ein einzelnes Zeichen im String

-----------------------------------------------------------
Beispiel aus der Aufgabe
-----------------------------------------------------------
Wir:
1) öffnen eine Textdatei
2) lesen den gesamten Inhalt
3) geben jedes Zeichen aus
4) zählen alle Zeichen
"""

from os import strerror

try:
    zaehler = 0                              # Zeichen-Zähler initialisieren
    stream = open("text.txt", "rt")          # Datei im Text-Lesemodus öffnen
    inhalt = stream.read()                   # Gesamten Inhalt auf einmal lesen

    for zeichen in inhalt:                   # Über jedes Zeichen iterieren
        print(zeichen, end="")               # Zeichen ausgeben (ohne Zeilenumbruch)
        zaehler += 1                         # Zähler erhöhen

    stream.close()                           # Stream schließen
    print("\n\nCharacters in file:", zaehler)

except IOError as fehler:
    print("I/O error occurred:", strerror(fehler.errno))



"""
-----------------------------------------------------------
Was passiert hier?
-----------------------------------------------------------
• read() liefert einen kompletten String
• for-Schleife läuft über JEDES einzelne Zeichen
• Auch Leerzeichen und \\n zählen als Zeichen
• Der Zähler liefert die exakte Zeichenanzahl

-----------------------------------------------------------
⚠️ WICHTIG FÜR AUFGABEN / PRÜFUNG (EDUBE / PCAP)
-----------------------------------------------------------
• read() → kompletter Dateiinhalt als STRING
• for ch in content → Iteration über Zeichen
• Zeichen zählen = einfache Schleife + Zähler
• IOError kann beim Öffnen oder Lesen auftreten

-----------------------------------------------------------
Typische Prüfungsfallen:
-----------------------------------------------------------
• read() mit readlines() verwechseln
• glauben, dass read() zeilenweise liest (FALSCH)
• close() vergessen
• große Dateien unbedacht komplett einlesen

-----------------------------------------------------------
Merke:
-----------------------------------------------------------
read() ist bequem, aber nur für **kleine bis mittlere Dateien**
geeignet. Für große Dateien → zeilenweises Lesen!
"""
