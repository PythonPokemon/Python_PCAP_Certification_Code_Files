"""
Ausnahmen: Fortsetzung
Dieses Beispiel zeigt die empfohlene Python-Methode zur Behandlung
mehrerer möglicher Fehler mit getrennten except-Blöcken.

Mögliche Ergebnisse:

1) Der Benutzer gibt eine gültige, nicht-null Ganzzahl ein (z. B. 5)
   → Division ist möglich
   Ausgabe:
       0.2
       ENDE.

2) Der Benutzer gibt 0 ein
   → Division durch Null
   Ausgabe:
       Durch Null kann nicht geteilt werden.
       ENDE.

3) Der Benutzer gibt einen nicht-ganzzahligen Wert ein (z. B. "Hallo")
   → int() löst ValueError aus
   Ausgabe:
       Sie müssen einen ganzzahligen Wert eingeben.
       ENDE.

4) Der Benutzer bricht das Programm lokal ab (z. B. STRG + C)
   → KeyboardInterrupt
   Ausgabe:
       Oh je, etwas ist schiefgegangen...
       ENDE.

Python führt im try-Block riskanten Code aus.
Falls ein bestimmter Fehler entsteht, wird der passende except-Block ausgeführt.
Alle nicht explizit behandelten Fehler landen im allgemeinen except.
"""
# Mehrere except-Blöcke – empfohlene Methode
try:
    zahl = int(input("Geben Sie eine Zahl ein: "))
    ergebnis = 1 / zahl
    print(ergebnis)
except ZeroDivisionError:
    print("Durch Null kann nicht geteilt werden.")
except ValueError:
    print("Sie müssen einen ganzzahligen Wert eingeben.")
except:
    print("Oh je, etwas ist schiefgegangen...")

print("ENDE.")
