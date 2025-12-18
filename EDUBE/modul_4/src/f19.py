"""
Diagnose von Stromproblemen (Streams)
Fehlertexte mit os.strerror()

-----------------------------------------------------------
Problemstellung
-----------------------------------------------------------
Bei Datei- und Stream-Operationen können viele
unterschiedliche Fehler auftreten (Datei fehlt,
keine Rechte, zu viele offene Dateien usw.).

Bisherige Lösung:
• Fehlernummer (errno) abfragen
• viele if/elif-Zweige schreiben

→ Das ist korrekt, aber umständlich.

-----------------------------------------------------------
Vereinfachung: os.strerror()
-----------------------------------------------------------
Python stellt eine Hilfsfunktion bereit:

    os.strerror(errno)

• erwartet eine Fehlernummer (z. B. exc.errno)
• liefert eine menschenlesbare Fehlermeldung
• spart lange if/elif-Ketten

⚠️ WICHTIG:
• Wird ein unbekannter Fehlercode übergeben,
  löst strerror() eine ValueError aus.

-----------------------------------------------------------
Beispiel: klassische Variante mit errno
-----------------------------------------------------------
"""

import errno

try:
    stream = open("c:/users/user/Desktop/file.txt", "rt")   # Datei öffnen
    stream.close()                                         # Stream schließen

except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("Die Datei existiert nicht.")
    elif exc.errno == errno.EMFILE:
        print("Zu viele Dateien gleichzeitig geöffnet.")
    else:
        print("Unbekannter Fehlercode:", exc.errno)



"""
-----------------------------------------------------------
Vereinfachte Variante mit os.strerror()
-----------------------------------------------------------
• Keine Fallunterscheidung mehr nötig
• System liefert direkt den Klartext
"""

from os import strerror

try:
    stream = open("c:/users/user/Desktop/file.txt", "rt")   # Datei öffnen
    stream.close()

except Exception as exc:
    print("Datei konnte nicht geöffnet werden:",
          strerror(exc.errno))



"""
-----------------------------------------------------------
Was passiert hier?
-----------------------------------------------------------
• exc.errno enthält die numerische Fehlernummer
• strerror(exc.errno) wandelt sie in Text um
  (betriebssystemabhängig)
• ideal für kompakte Fehlermeldungen

-----------------------------------------------------------
⚠️ WICHTIG FÜR AUFGABEN / PRÜFUNG (EDUBE / PCAP)
-----------------------------------------------------------
• IOError / OSError besitzen das Attribut exc.errno
• os.strerror(errno) liefert eine verständliche Meldung
• spart komplexe if/elif-Fehlerbehandlung
• unbekannter Fehlercode → ValueError

-----------------------------------------------------------
Typische Prüfungsfallen:
-----------------------------------------------------------
• exc.errno vergessen auszuwerten
• Fehlertext selbst „nachbauen“, obwohl strerror() existiert
• glauben, strerror() funktioniert ohne errno

-----------------------------------------------------------
Merke:
-----------------------------------------------------------
errno        → maschinenlesbarer Fehlercode  
strerror()   → menschenlesbare Fehlermeldung  

Beides zusammen ergibt saubere Fehlerdiagnose.
"""
