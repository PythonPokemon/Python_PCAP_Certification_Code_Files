"""
Verarbeitung von Textdateien
Grundlagen des Lesens von Textdateien in Python

-----------------------------------------------------------
Was ist das Ziel dieser Aufgabe?
-----------------------------------------------------------
Wir wollen:
• eine einfache Textdatei öffnen
• ihren kompletten Inhalt lesen
• den Inhalt auf der Konsole ausgeben
• (optional) die Anzahl der gelesenen Zeichen ermitteln

Dabei gehen wir von einer **reinen Textdatei** aus:
• keine Formatierungen
• keine Schriftarten
• keine Office-Dokumente

-----------------------------------------------------------
Wichtige Voraussetzung
-----------------------------------------------------------
Textdateien sollten mit einfachen Editoren erstellt werden:
• Notepad
• Vim
• Gedit
• Nano

❌ Keine Textverarbeitungsprogramme wie:
• MS Word
• LibreOffice Writer

-----------------------------------------------------------
Textkodierung (Encoding)
-----------------------------------------------------------
Wenn die Datei **Sonderzeichen** enthält (z. B. Umlaute),
muss beim Öffnen die richtige Kodierung angegeben werden.

Typisch (Unix / Linux / moderne Systeme):
    UTF-8

Syntax:
    open(dateiname, modus, encoding="utf-8")

-----------------------------------------------------------
Beispiel aus der Aufgabe
-----------------------------------------------------------
Wir öffnen eine Textdatei, lesen den gesamten Inhalt
und geben ihn auf der Konsole aus.
"""
stream = open("C:\\Users\\Jakob.Derzapf\\OneDrive - Amadeus Fire AG\Dokumente\\Python_PCAP_Certification_Code_Files\EDUBE\\modul_4\\src\\tzop.txt", "rt", encoding="utf-8")
#stream = open("tzop.txt", "rt", encoding="utf-8")   # Textdatei im Lesemodus öffnen
inhalt = stream.read()                              # Gesamten Dateiinhalt lesen
stream.close()                                      # Stream schließen

print(inhalt)                                       # Dateiinhalt ausgeben



"""
-----------------------------------------------------------
Was passiert hier?
-----------------------------------------------------------
• open(...) öffnet die Datei im Textmodus ("rt")
• encoding="utf-8" sorgt für korrekte Zeichendarstellung
• read() liest ALLES auf einmal (inkl. Zeilenumbrüche)
• close() schließt den Stream und gibt Ressourcen frei

-----------------------------------------------------------
⚠️ WICHTIG FÜR AUFGABEN / PRÜFUNG (EDUBE / PCAP)
-----------------------------------------------------------
• Textdateien werden im Modus "rt" geöffnet
• read() liest den kompletten Inhalt als STRING
• Sonderzeichen → encoding angeben!
• Vergessen von close() gilt als schlechter Stil

-----------------------------------------------------------
Typische Prüfungsfallen:
-----------------------------------------------------------
• Datei mit Word erstellt → kein reiner Text
• encoding vergessen → UnicodeDecodeError
• Datei nicht geschlossen
• read() mit readlines() verwechselt

-----------------------------------------------------------
Merke:
-----------------------------------------------------------
Textdatei + open() + "rt" + encoding
→ Ergebnis ist IMMER ein String
"""
