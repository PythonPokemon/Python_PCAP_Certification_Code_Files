"""
Diagnose von Stromproblemen (fortgesetzt)
Fehlerbehandlung mit errno vs. os.strerror()

-----------------------------------------------------------
Problemstellung
-----------------------------------------------------------
Beim Arbeiten mit Dateien (Streams) können viele verschiedene
Fehler auftreten, z. B.:

• Datei existiert nicht
• Keine Zugriffsrechte
• Zu viele Dateien gleichzeitig geöffnet

Python liefert in solchen Fällen eine Ausnahme (OSError /
IOError), die eine **Fehlernummer (errno)** enthält.

-----------------------------------------------------------
Klassischer Ansatz: Fehlernummer manuell auswerten
-----------------------------------------------------------
Man prüft exc.errno und reagiert mit if/elif-Anweisungen.

Vorteil:
• Sehr präzise Kontrolle

Nachteil:
• Viel Code
• Unübersichtlich bei vielen Fehlerfällen
"""

import errno

try:
    stream = open("c:/users/user/Desktop/file.txt", "rt")   # Datei öffnen
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
Python stellt die Funktion os.strerror() bereit.

Syntax:
    strerror(errno)

• erwartet eine Fehlernummer (exc.errno)
• liefert eine menschenlesbare Beschreibung
• spart lange if/elif-Ketten

⚠️ Hinweis:
• Wird ein unbekannter Fehlercode übergeben,
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
• Die Fehlermeldung ist betriebssystemabhängig
• Ideal für kompakte und saubere Fehlerausgaben

-----------------------------------------------------------
⚠️ WICHTIG FÜR AUFGABEN / PRÜFUNG (EDUBE / PCAP)
-----------------------------------------------------------
• Datei-/Stream-Fehler sind OSError / IOError
• Diese besitzen das Attribut exc.errno
• os.strerror() vereinfacht die Fehlerdiagnose erheblich
• Unbekannter Fehlercode → ValueError

-----------------------------------------------------------
Typische Prüfungsfallen:
-----------------------------------------------------------
• exc.errno nicht verwenden
• Fehlertexte selbst „nachbauen“
• os.strerror() ohne Fehlernummer aufrufen

-----------------------------------------------------------
Merke:
-----------------------------------------------------------
errno        → maschinenlesbarer Fehlercode  
strerror()   → menschenlesbare Fehlermeldung  

Beides zusammen = saubere Stream-Fehlerdiagnose.
"""
