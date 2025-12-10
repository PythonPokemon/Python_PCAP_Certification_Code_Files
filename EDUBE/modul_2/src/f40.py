"""
Fehler, Ausnahmen und andere Pannen
-----------------------------------------------------------------
Alles, was schiefgehen KANN, wird irgendwann schiefgehen.
(Murphy’s Gesetz)

Auch die Ausführung deines Codes kann unerwartet scheitern.

Im folgenden Beispiel gibt es zwei typische Fehlerquellen:

1) Der Benutzer kann beliebigen Text eingeben.
   → Die Eingabe lässt sich dann evtl. NICHT in float umwandeln.
   → Dies führt zu ValueError: could not convert string to float

2) Die Funktion sqrt() darf KEINE negativen Zahlen erhalten.
   → Bei negativen Werten entsteht ValueError: math domain error

Beispielproblem:

Eingabe: Abracadabra
→ float() kann dies nicht umwandeln → ValueError

Eingabe: -1
→ math.sqrt(-1) ist mathematisch undefiniert → ValueError

Fazit:
Ein guter Programmierer schützt seinen Code vor solchen Fehlern.
"""
import math

x = float(input("Geben Sie x ein: "))
y = math.sqrt(x)

print("Die Quadratwurzel von", x, "ist", y)
