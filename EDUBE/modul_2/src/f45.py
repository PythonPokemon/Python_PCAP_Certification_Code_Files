"""
Ausnahmen: Fortsetzung
Dieses Beispiel zeigt deutlich, wie try/except den Programmfluss verändert.

Ablauf des Codes:
1) Die erste Ausgabe „1“ wird ausgeführt.
2) Anschließend kommt die Division durch 0 → ZeroDivisionError.
3) Der Rest des try-Blocks (print("2")) wird übersprungen.
4) Der except-Block wird ausgeführt:
       → „Oh dear, something went wrong...“
5) Nach dem except-Block geht das Programm normal weiter.
       → Ausgabe „3“

Wichtig:
Jeder Code NACH der fehlerauslösenden Zeile im try-Block
wird NICHT MEHR ausgeführt.
"""
# Demonstration des Verhaltens von try/except
try:
    print("1")
    x = 1 / 0          # Fehler → Division durch Null
    print("2")         # Wird NICHT ausgeführt
except:
    print("Oh ne, etwas ist schiff gelaufen...")

print("3")             # Wird IMMER ausgeführt
