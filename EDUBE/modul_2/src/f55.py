"""
Ausnahmen: Fortsetzung
Jetzt lernen wir eine neue Python-Anweisung kennen: assert.
Dies ist ein Python-Schlüsselwort.

Verwendung:
    assert Ausdruck

Funktionsweise:
1) Der Ausdruck wird ausgewertet.
2) Wenn der Ausdruck TRUE ist (oder ein nicht-leerer String, eine nicht-0 Zahl usw.),
   → passiert nichts.
3) Wenn der Ausdruck FALSE ergibt,
   → löst Python automatisch eine AssertionError-Ausnahme aus.
     (Man sagt dann: „Die Assertion ist fehlgeschlagen“.)

Wofür nutzt man assert?
• Um Stellen im Code abzusichern, an denen falsche Werte absolut NICHT
  toleriert werden können.
• Besonders sinnvoll in Funktionen, die von anderen benutzt werden.
• Ein AssertionError zeigt sehr deutlich:
      „Hier ist eine Bedingung verletzt worden, die IMMER gelten muss.“

Wichtig:
• assert ersetzt KEINE Fehlerbehandlung.
• assert validiert NICHT Eingaben.
• assert ist ein Zusatz-Sicherheitsnetz — ähnlich wie ein Airbag:
  Du hoffst, dass er nie auslöst, aber wenn doch, verhindert er größeren Schaden.

Beispiel aus dem Programm:
--------------------------
• Das Programm funktioniert fehlerfrei, wenn der Nutzer eine Zahl >= 0 eingibt.
• Bei einer negativen Zahl löst assert x >= 0.0 einen AssertionError aus.

Fehlerausgabe:
Traceback (most recent call last):
  File ".main.py", line 4, in <module>
    assert x >= 0.0
AssertionError
"""
import math

zahl = float(input("Geben Sie eine Zahl ein: "))
assert zahl >= 0.0          # Bricht ab, wenn die Zahl negativ ist

wurzel = math.sqrt(zahl)
print(wurzel)
