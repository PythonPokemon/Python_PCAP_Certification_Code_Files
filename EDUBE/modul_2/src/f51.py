"""
Ausnahmen: Fortsetzung
Dieses Beispiel zeigt, warum die REIHENFOLGE der except-Blöcke entscheidend ist.

Fall 1: Spezifische Ausnahme zuerst
----------------------------------
Der Code hat zuerst einen except ZeroDivisionError-Zweig,
danach einen allgemeineren except ArithmeticError.

Die ausgelöste Ausnahme ist ZeroDivisionError.
Der erste passende Zweig ist also:

    except ZeroDivisionError:

Ausgabe:
    Zero Division!
    ENDE.


Fall 2: Allgemeine Ausnahme zuerst
----------------------------------
Wenn wir die Reihenfolge vertauschen und zuerst schreiben:

    except ArithmeticError:

fängt dieser Zweig ebenfalls ZeroDivisionError ab,
denn ZeroDivisionError ist eine Unterklasse von ArithmeticError.

Die speziellere Ausnahme ZeroDivisionError wird jetzt NIE erreicht —
sie ist „tot“ bzw. „unreachable“.

Ausgabe:
    Arithmetic problem!
    ENDE.

Wichtige Regeln:
----------------
1) Die Reihenfolge der except-Zweige ist WICHTIG.
2) Stelle niemals eine allgemeinere Ausnahme (z. B. ArithmeticError, Exception)
   vor eine speziellere (z. B. ZeroDivisionError).
3) Allgemeinere Fehler vor spezifischeren machen die späteren Zweige nutzlos.
4) Python warnt NICHT vor solchen Fehlern — der Programmierer muss selbst aufpassen.
"""
# Beispiel: korrekte Reihenfolge (spezifisch → allgemein)
try:
    ergebnis = 1 / 0
except ZeroDivisionError:
    print("Zero Division!")
except ArithmeticError:
    print("Arithmetic problem!")

print("ENDE.")


# Beispiel: falsche Reihenfolge (allgemein → spezifisch)
try:
    ergebnis = 1 / 0
except ArithmeticError:  # fängt auch ZeroDivisionError ab
    print("Arithmetic problem!")
except ZeroDivisionError:  # wird nie erreicht
    print("Zero Division!")

print("ENDE.")
