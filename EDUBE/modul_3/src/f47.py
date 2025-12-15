"""
Mehr zu Ausnahmen – try / except / else

Der try–except–Block kann um einen else-Zweig erweitert werden.

Wichtige Regel:
- try:      → hier steht der „gefährliche“ Code
- except:   → wird ausgeführt, WENN eine Ausnahme auftritt
- else:     → wird NUR ausgeführt, WENN KEINE Ausnahme auftritt

Genau EIN Pfad wird durchlaufen:
- entweder except
- oder else
---------------------------------------------------------------
Merksatz (prüfungsrelevant, PCAP):

    else gehört zu try, nicht zu except
    else läuft nur, wenn keine Ausnahme auftritt
    else ersetzt keine Fehlerbehandlung, sondern ergänzt sie
"""

def kehrwert(zahl):
    try:
        ergebnis = 1 / zahl                          # kritische Operation (Division)
    except ZeroDivisionError:
        print("Division fehlgeschlagen")             # Fehlerbehandlung
        return None                                  # Abbruch bei Fehler
    else:
        print("Alles gut gelaufen")                  # läuft nur, wenn KEIN Fehler auftrat
        return ergebnis                              # korrektes Ergebnis zurückgeben


print(kehrwert(2))                                   # kein Fehler → else-Zweig
print(kehrwert(0))                                   # ZeroDivisionError → except-Zweig
