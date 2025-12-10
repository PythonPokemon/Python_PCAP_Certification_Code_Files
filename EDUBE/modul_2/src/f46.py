"""
Ausnahmen: Fortsetzung
Ein Nachteil eines einzelnen allgemeinen except-Blocks ist:
Er sagt NICHTS darüber aus, *welcher* Fehler passiert ist.

Im Beispiel unten kann es zwei Ursachen geben:

1) Der Benutzer gibt keinen ganzzahligen Wert ein
   → Fehler: ValueError

2) Der Benutzer gibt 0 ein
   → Fehler: ZeroDivisionError (Division durch 0)

Da except: alle Fehler abfängt, erscheint immer dieselbe Meldung:
"Oh dear, something went wrong..."

Man weiß also nicht, *warum* der Fehler entstanden ist.

Technisch gibt es zwei Lösungen:

----------------------------------------------------
1) Zwei getrennte try-Blöcke (funktioniert, ist aber unschön)
----------------------------------------------------

----------------------------------------------------
2) Bessere Lösung: mehrere except-Blöcke
   Syntax:

try:
    ...
except FehlerTyp1:
    ...
except FehlerTyp2:
    ...
except:
    ...   # optionaler allgemeiner Block
----------------------------------------------------

Funktionsweise:
• Wenn im try-Block FehlerTyp1 entsteht → except FehlerTyp1 wird ausgeführt.
• Wenn FehlerTyp2 entsteht → except FehlerTyp2 wird ausgeführt.
• Wenn ein anderer Fehler entsteht → der letzte allgemeine except greift.
"""
# Beispielcode: undifferenzierte Fehlerbehandlung (schlechte Variante)
try:
    x = int(input("Geben Sie eine Zahl ein: "))
    y = 1 / x
except:
    print("Oh dear, something went wrong...")

print("ENDE.")
