"""
Ausnahmen: Fortsetzung
Wichtige Regeln für except-Blöcke:

1) Die except-Blöcke werden in der Reihenfolge geprüft,
   in der sie im Code stehen.

2) Du darfst NICHT zwei except-Blöcke mit demselben
   Fehlertyp verwenden.

3) Die Anzahl der verschiedenen except-Blöcke ist beliebig –
   aber: zu jedem try muss mindestens EIN except gehören.

4) Das Schlüsselwort except darf NIEMALS ohne vorheriges try stehen.

5) Wenn ein except-Block ausgeführt wird, werden ALLE weiteren
   except-Blöcke übersprungen.

6) Wenn KEIN except-Block zur ausgelösten Ausnahme passt,
   bleibt die Ausnahme unbehandelt (und das Programm stürzt ab).

7) Ein allgemeiner except (ohne Fehlernamen) MUSS immer
   als LETZTER except stehen.

Beispiel-Schema:

try:
    ...
except Fehler1:
    ...
except Fehler2:
    ...
except:
    ...   # allgemeiner Block für alle anderen Fehler


-------------------------------------------
Experiment aus dem Programmtext:
-------------------------------------------

Wir entfernen den ZeroDivisionError-Block.

Was passiert, wenn der Benutzer 0 eingibt?

→ Es entsteht ein ZeroDivisionError.
→ Da kein spezieller Block mehr existiert,
   landet die Ausnahme im allgemeinen except.
→ Ausgabe:
       Oh je, etwas ist schiefgegangen...
       ENDE.
"""
# Beispiel: ZeroDivisionError wird NICHT mehr separat behandelt
try:
    zahl = int(input("Geben Sie eine Zahl ein: "))
    ergebnis = 1 / zahl
    print(ergebnis)
except ValueError:
    print("Sie müssen einen ganzzahligen Wert eingeben.")
except:
    print("Oh je, etwas ist schiefgegangen...")

print("ENDE.")
