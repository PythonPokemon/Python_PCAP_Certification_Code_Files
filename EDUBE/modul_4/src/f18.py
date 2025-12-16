"""
Schließende Bäche (Streams)
Stream schließen & Fehlerdiagnose mit errno

-----------------------------------------------------------
Warum muss ein Stream geschlossen werden?
-----------------------------------------------------------
Die LETZTE Operation auf einem Stream sollte IMMER
das Schließen sein.

Ausnahme:
• sys.stdin
• sys.stdout
• sys.stderr
(diese sind bereits vom System verwaltet)

Schließen erfolgt mit:
    stream.close()

-----------------------------------------------------------
Was macht close() genau?
-----------------------------------------------------------
• trennt die Verbindung zwischen Programm und Datei
• gibt Betriebssystem-Ressourcen frei
• erzwingt das Schreiben gepufferter Daten (Flush)

⚠️ WICHTIG:
Beim Schreiben können Daten noch im Puffer liegen.
Erst close() erzwingt das endgültige Schreiben
auf das physische Medium.

-----------------------------------------------------------
Eigenschaften von close()
-----------------------------------------------------------
• erwartet KEINE Argumente
• gibt KEINEN Rückgabewert zurück
• kann eine IOError-Ausnahme auslösen
  (z. B. beim Flush von Puffern)

-----------------------------------------------------------
Beispiel: Datei öffnen, schreiben und schließen
"""

try:
    stream = open("beispiel.txt", "wt")           # Datei zum Schreiben öffnen
    stream.write("Hallo Datei!\n")                # Daten schreiben
    stream.write("Noch eine Zeile.\n")
    stream.close()                                # Stream schließen (wichtig!)

except IOError as exc:
    print("Fehler beim Arbeiten mit der Datei:", exc)



"""
-----------------------------------------------------------
Warum können Fehler beim Schließen auftreten?
-----------------------------------------------------------
• Schreiboperationen werden gepuffert (Buffering)
• close() erzwingt das Flushen der Puffer
• schlägt das Flushen fehl → IOError

Deshalb ist es FALSCH zu glauben, dass close()
IMMER fehlerfrei ist.

-----------------------------------------------------------
Diagnose von Stream-Fehlern
-----------------------------------------------------------
IOError-Objekte besitzen das Attribut:
    exc.errno

errno = Error Number (Fehlernummer)

Damit kann die genaue Ursache ermittelt werden.
"""

import errno

try:
    stream = open("beispiel.txt", "wt")
    stream.write("Test")
    stream.close()

except IOError as exc:
    print("Fehlernummer:", exc.errno)

    if exc.errno == errno.EACCES:
        print("Zugriff verweigert")
    elif exc.errno == errno.ENOSPC:
        print("Kein Speicherplatz mehr")
    else:
        print("Anderer Datei-Fehler")



"""
-----------------------------------------------------------
Wichtige errno-Konstanten (Auswahl)
-----------------------------------------------------------
errno.EACCES   → Berechtigung verweigert
errno.EBADF    → Ungültiger Dateihandle
errno.EEXIST   → Datei existiert bereits
errno.EFBIG    → Datei zu groß
errno.EISDIR   → Pfad ist ein Verzeichnis
errno.EMFILE   → Zu viele offene Dateien
errno.ENOENT   → Datei/Verzeichnis existiert nicht
errno.ENOSPC   → Kein Speicherplatz mehr

-----------------------------------------------------------
⚠️ WICHTIG FÜR AUFGABEN / PRÜFUNG (EDUBE / PCAP)
-----------------------------------------------------------
• Jeder geöffnete Stream MUSS geschlossen werden
• close() kann Fehler auslösen (IOError)
• Fehlerdetails stehen in exc.errno
• errno-Werte werden mit errno.<KONSTANTE> verglichen

-----------------------------------------------------------
Typische Prüfungsfallen:
-----------------------------------------------------------
• Datei öffnen, aber nicht schließen
• Annehmen, dass close() nie fehlschlägt
• IOError fangen, aber errno ignorieren
• sys.stdin / stdout / stderr fälschlich schließen

-----------------------------------------------------------
Merke:
-----------------------------------------------------------
open()  → Ressource belegen  
close() → Ressource freigeben  

Stream schließen ist Pflicht – nicht Kür.
"""
