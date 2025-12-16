"""
Lambda-Funktion – anonyme Funktionen in Python

-----------------------------------------------------------
Was ist eine Lambda-Funktion?
-----------------------------------------------------------
Eine lambda-Funktion ist eine **anonyme Funktion** – also eine
Funktion ohne Namen. Sie wird verwendet, um extrem kurze,
einfache Funktionen direkt im Code zu definieren, ohne
def-Block.

Syntax:
    lambda parameter: ausdruck

Der Ausdruck wird automatisch zurückgegeben.

-----------------------------------------------------------
Warum gibt es Lambdas?
-----------------------------------------------------------
• vereinfachen Code, wenn Funktionen nur EINMAL benötigt werden  
• ideal in Kombination mit:
  - sort()
  - map()
  - filter()
  - reduce()
• kompakt und lesbarer als kleine def-Funktionen

-----------------------------------------------------------
Beispiele aus der Aufgabe
-----------------------------------------------------------
"""
two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))


"""
-----------------------------------------------------------
Was passiert hier?
-----------------------------------------------------------
• two        → lambda ohne Parameter, liefert immer 2
• sqr(x)     → Quadratfunktion
• pwr(x, y)  → Potenzfunktion

Alle drei Lambdas könnten durch def ersetzt werden – aber
Lambdas machen den Code kürzer und unmittelbarer.

-----------------------------------------------------------
⚠️ PCAP-WICHTIG:
-----------------------------------------------------------
• lambda darf NUR einen Ausdruck enthalten (keine Anweisungen)
• return gibt es nicht – der Ausdruck ist automatisch Rückgabewert
• lambda erzeugt immer genau EINEN Wert, keine Anweisungen, keine Blöcke
• Lambdas sind Funktionen wie jede andere – nur ohne Namen

-----------------------------------------------------------
Typische Prüfungsfalle:
-----------------------------------------------------------
lambda x: print(x)
→ gültig, aber der Ausdruck liefert None zurück, weil print() None ist

lambda x: x if x > 0 else -x
→ gültiger Ausdruck

lambda x: (x := x + 1)
→ neu in Python 3.8, aber NICHT prüfungsrelevant

-----------------------------------------------------------
Merke:
-----------------------------------------------------------
Lambdas sind NICHT stärker als def – nur kürzer, situativ nützlicher.
"""
