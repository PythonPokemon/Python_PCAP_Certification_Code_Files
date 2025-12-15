"""
Mehr zu Ausnahmen – try / except / else / finally

Der try-Block kann um einen finally-Zweig erweitert werden.

Wichtige Eigenschaften von finally:
- finally wird IMMER ausgeführt
- egal ob:
  - keine Ausnahme auftritt
  - eine Ausnahme auftritt
  - die Ausnahme behandelt wurde oder nicht
- finally eignet sich für:
  - Aufräumarbeiten (Dateien schließen, Verbindungen beenden, Locks freigeben)

⚠️ Achtung (prüfungsrelevant):
Ein return im finally-Block überschreibt jedes return aus try / except / else.
"""

def kehrwert(zahl):
    try:
        ergebnis = 1 / zahl                          # kritische Operation
    except ZeroDivisionError:
        print("Division fehlgeschlagen")             # Fehlerfall
        ergebnis = None                              # definiertes Fehlerergebnis
    else:
        print("Alles gut gelaufen")                  # nur bei erfolgreicher Division
    finally:
        print("Jetzt wird aufgeräumt")               # läuft IMMER
        return ergebnis                              # überschreibt alle vorherigen returns


print(kehrwert(2))                                   # → else + finally
print(kehrwert(0))                                   # → except + finally
