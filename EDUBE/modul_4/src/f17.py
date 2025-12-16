"""
Eröffnung eines Dateistreams & vordefinierte Streams (stdin / stdout / stderr)

-----------------------------------------------------------
Datei zum ersten Mal öffnen – Grundidee
-----------------------------------------------------------
Bevor man aus einer Datei lesen oder in sie schreiben kann,
MUSS sie mit der Funktion open() geöffnet werden.

Das Öffnen kann fehlschlagen (z. B.:
• Datei existiert nicht
• falscher Pfad
• fehlende Zugriffsrechte)

➡️ Deshalb wird open() sehr häufig in einem try/except-Block
verwendet.

-----------------------------------------------------------
Beispiel: Textdatei zum Lesen öffnen
-----------------------------------------------------------
Wir wollen die Datei:
C:\\Users\\Jakob.Derzapf\\OneDrive - Amadeus Fire AG\\Dokumente\\Python_PCAP_Certification_Code_Files\\EDUBE\\modul_4\src\\file.txt
im Textmodus lesen.

Modus:
• "r"  → read (lesen)
• "t"  → text (Standard, kann weggelassen werden)
"""

try:
    stream = open("C:\\Users\\Jakob.Derzapf\\OneDrive - Amadeus Fire AG\\Dokumente\\Python_PCAP_Certification_Code_Files\\EDUBE\\modul_4\src\\file.txt", "rt")  # Datei öffnen (Text + Lesen)

    # Verarbeitung der Datei
    inhalt = stream.read()                                    # gesamten Inhalt lesen
    print(inhalt)                                             # Ausgabe auf stdout

    stream.close()                                            # Stream IMMER schließen

except Exception as exc:
    print("Cannot open the file:", exc)                        # Fehlermeldung ausgeben



"""
-----------------------------------------------------------
Was passiert hier Schritt für Schritt?
-----------------------------------------------------------
• try-Block:
  - schützt vor Laufzeitfehlern beim Öffnen der Datei

• open(...):
  - versucht, die Datei zu öffnen
  - bei Erfolg → gibt ein Stream-Objekt zurück
  - bei Fehler → wirft eine Exception

• stream.close():
  - trennt die Verbindung zwischen Programm und Datei
  - MUSS nach der Arbeit mit der Datei erfolgen

• except Exception as exc:
  - fängt ALLE Öffnungs- und Zugriffsfehler ab
  - exc enthält die konkrete Fehlermeldung

-----------------------------------------------------------
Vorgeöffnete Streams in Python
-----------------------------------------------------------
Nicht alle Streams müssen mit open() geöffnet werden.

Beim Start eines Python-Programms sind DREI Streams
bereits geöffnet. Sie befinden sich im Modul sys.
"""

import sys



"""
-----------------------------------------------------------
sys.stdin  – Standard-Eingabe
-----------------------------------------------------------
• normalerweise mit der Tastatur verbunden
• dient zum Lesen von Eingaben

Die Funktion input() liest STANDARDMÄSSIG aus sys.stdin.
"""

eingabe = sys.stdin.readline()        # eine Zeile von der Tastatur lesen
print("Eingabe war:", eingabe)



"""
-----------------------------------------------------------
sys.stdout – Standard-Ausgabe
-----------------------------------------------------------
• normalerweise mit dem Bildschirm verbunden
• dient zur Ausgabe von Programmerkennissen

Die Funktion print() schreibt STANDARDMÄSSIG nach sys.stdout.
"""

sys.stdout.write("Hallo von stdout\n")



"""
-----------------------------------------------------------
sys.stderr – Standard-Fehlerausgabe
-----------------------------------------------------------
• ebenfalls meist mit dem Bildschirm verbunden
• gedacht für FEHLER- und WARNMELDUNGEN
• getrennt von der normalen Programmausgabe

Warum wichtig?
• stdout und stderr können getrennt umgeleitet werden
  (z. B. in Dateien oder Logs)
"""

sys.stderr.write("Dies ist eine Fehlermeldung!\n")



"""
-----------------------------------------------------------
⚠️ WICHTIG FÜR AUFGABEN / PRÜFUNG (EDUBE / PCAP)
-----------------------------------------------------------
• Jede Dateioperation beginnt mit open()
• open() kann eine Exception auslösen → try/except verwenden
• Streams MÜSSEN nach Benutzung geschlossen werden

• Bereits geöffnete Streams:
  - sys.stdin   → Eingabe
  - sys.stdout  → normale Ausgabe
  - sys.stderr  → Fehlerausgabe

• input() liest aus stdin
• print() schreibt nach stdout

-----------------------------------------------------------
Typische Prüfungsfallen:
-----------------------------------------------------------
• Backslashes im Windows-Pfad nicht escapen → FEHLER
  → richtig: "C:\\Users\\Jakob.Derzapf\\OneDrive - Amadeus Fire AG\\Dokumente\\Python_PCAP_Certification_Code_Files\\EDUBE\\modul_4\src\\file.txt"

• Datei nicht schließen → Ressourcenproblem
• Annahme, dass print() immer auf den Bildschirm geht
  → stdout kann umgeleitet sein

-----------------------------------------------------------
Merke:
-----------------------------------------------------------
open() → Datei-Stream  
stdin / stdout / stderr → immer verfügbar  

Dateien brauchen open() – Standardstreams nicht.
"""
