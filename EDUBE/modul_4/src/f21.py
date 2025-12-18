"""
Diagnose von Stromproblemen (fortgesetzt)
Fehlercodes verstehen und vereinfachen mit os.strerror()

-----------------------------------------------------------
Problemstellung
-----------------------------------------------------------
Beim Arbeiten mit Dateien (Streams) können zahlreiche
Laufzeitfehler auftreten, z. B.:

• Datei existiert nicht
• Keine Zugriffsrechte
• Zu viele Dateien gleichzeitig geöffnet

Diese Fehler werden in Python als OSError / IOError ausgelöst
und enthalten eine **numerische Fehlernummer (errno)**.

-----------------------------------------------------------
Klassischer Ansatz: Fehlernummer manuell prüfen
-----------------------------------------------------------
Man wertet exc.errno aus und reagiert mit if / elif.

Vorteil:
• Sehr präzise Kontrolle über einzelne Fehlerfälle

Nachteil:
• Viel Code
• Schlechte Skalierbarkeit
"""

import errno

try:
    stream = open("c:/users/user/Desktop/file.txt", "rt")   # Datei im Textmodus öffnen
    stream.close()                                         # Stream schließen

except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist.")
    elif exc.errno == errno.EMFILE:
        print("You've opened too many files.")
    else:
        print("The error number is:", exc.errno)



"""
-----------------------------------------------------------
Vereinfachter Ansatz: os.strerror()
-----------------------------------------------------------
Das Modul os stellt die Funktion strerror() bereit.

Syntax:
    strerror(errno)

• erwartet eine Fehlernummer (exc.errno)
• liefert eine menschenlesbare Beschreibung
• ersetzt lange if/elif-Ketten

⚠️ Hinweis:
• Wird ein ungültiger Fehlercode übergeben,
  löst strerror() eine ValueError-Ausnahme aus.
"""

from os import strerror

try:
    stream = open("c:/users/user/Desktop/file.txt", "rt")   # Datei öffnen
    stream.close()

except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))



"""
-----------------------------------------------------------
Was passiert hier?
-----------------------------------------------------------
• exc.errno enthält den numerischen Fehlercode
• strerror(exc.errno) übersetzt ihn in Klartext
• Die Ausgabe ist betriebssystemabhängig
• Ideal für kompakte und saubere Fehlermeldungen

-----------------------------------------------------------
⚠️ WICHTIG FÜR AUFGABEN / PRÜFUNG (EDUBE / PCAP)
-----------------------------------------------------------
• Datei-Fehler sind OSError / IOError
• Diese besitzen immer das Attribut errno
• os.strerror() ist der empfohlene Weg für Fehlermeldungen
• Ungültiger errno-Wert → ValueError

-----------------------------------------------------------
Typische Prüfungsfallen:
-----------------------------------------------------------
• exc.errno vergessen
• Fehlertexte manuell definieren
• strerror() ohne errno aufrufen

-----------------------------------------------------------
Merke:
-----------------------------------------------------------
errno        → maschinenlesbarer Fehlercode  
strerror()   → menschenlesbare Fehlermeldung  

Zusammen liefern sie eine saubere Stream-Diagnose.
"""
