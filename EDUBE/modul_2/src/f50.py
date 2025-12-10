"""
Ausnahmen: Fortsetzung
Dieses Beispiel zeigt, wie Python Ausnahmen anhand ihrer
Vererbungs-Hierarchie behandelt.

Im ersten Beispiel wird ZeroDivisionError explizit abgefangen.
Die Ausgabe lautet:

Oooppsss...
ENDE.

Nun ersetzen wir ZeroDivisionError durch ArithmeticError.

Wichtig:
• ZeroDivisionError ist eine Unterklasse von ArithmeticError.
• ArithmeticError ist also allgemeiner.
• Daher wird auch der ZeroDivisionError von ArithmeticError abgefangen.

Das Programmverhalten bleibt also IDENTISCH.

Noch allgemeiner:
• BaseException fängt ALLE Ausnahmen ab.
• Exception ist ebenfalls sehr allgemein und deckt fast alle üblichen Fehler ab.

Wesentliche Regeln:
1) Jede ausgelöste Ausnahme wird dem ERSTEN passenden except-Zweig zugeordnet.
2) Der except-Zweig muss NICHT exakt denselben Fehlernamen besitzen.
   Es genügt, wenn er allgemeiner ist (eine Oberklasse des Fehlertyps).

Dieses Verhalten basiert auf der Vererbungshierarchie der Exceptions.
"""
# Beispiel 1: Spezifische Ausnahme (ZeroDivisionError)
try:
    ergebnis = 1 / 0
except ZeroDivisionError:
    print("Oooppsss...")

print("ENDE.")


# Beispiel 2: Allgemeinere Ausnahme (ArithmeticError)
try:
    ergebnis = 1 / 0
except ArithmeticError:   # fängt auch ZeroDivisionError ab
    print("Oooppsss...")

print("ENDE.")
