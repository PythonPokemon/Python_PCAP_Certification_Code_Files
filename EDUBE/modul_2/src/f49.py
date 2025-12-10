"""
Ausnahmen: Fortsetzung
Wir verschlechtern erneut absichtlich den Code, um das Verhalten zu beobachten.

Diesmal haben wir den allgemeinen except-Block entfernt.
Es existiert nur noch ein spezieller except für ValueError.

Was passiert nun, wenn der Benutzer 0 eingibt?

1) 0 löst eine Division durch Null aus → ZeroDivisionError
2) ZeroDivisionError passt NICHT zu ValueError
3) Es gibt KEINEN anderen except-Block
4) Die Ausnahme bleibt unbehandelt

Ergebnis:
Python bricht das Programm ab und zeigt eine vollständige Fehlermeldung an:

Traceback (most recent call last):
  File "exc.py", line 3, in <module>
    y = 1 / x
ZeroDivisionError: division by zero

Damit solltest du nun verstanden haben:
Wenn keine passende except-Klausel existiert,
bleibt die Ausnahme unbehandelt und das Programm stürzt ab.

Im nächsten Kapitel geht es weiter mit den eingebauten Python-Ausnahmen
und ihrer Hierarchie.
"""
# Beispiel: ZeroDivisionError wird NICHT abgefangen
try:
    zahl = int(input("Geben Sie eine Zahl ein: "))
    ergebnis = 1 / zahl
    print(ergebnis)
except ValueError:
    print("Sie müssen einen ganzzahligen Wert eingeben.")

print("ENDE.")
