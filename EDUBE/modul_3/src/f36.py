"""
Wie Python Eigenschaften und Methoden findet – Fortsetzung
Suchreihenfolge bei Attributen und Methoden (MRO-Grundprinzip)
-----------------------------------------------------

Wenn du auf eine Eigenschaft oder Methode eines Objekts zugreifst, sucht
Python sie immer in einer festen Reihenfolge:

-----------------------------------------------------------
Suchreihenfolge (vereinfacht)
-----------------------------------------------------------
1) Zuerst im Objekt selbst
   → also in den Instanzvariablen (objekt.__dict__)

2) Danach in der Klasse des Objekts und ihren Superklassen
   → von unten nach oben entlang der Vererbungskette
   → das betrifft:
      - Klassenvariablen
      - Methoden

3) Wenn Python nichts findet:
   → AttributeError wird ausgelöst

-----------------------------------------------------------
Wichtig:
-----------------------------------------------------------
Objekte können nachträglich Attribute bekommen (z.B. objekt.neu = 5).
Darum können zwei Objekte derselben Klasse unterschiedliche Attribute besitzen.

-----------------------------------------------------------
Beispiel: 3-stufige Vererbung
-----------------------------------------------------------
Wir bauen eine Vererbungskette:

Level1 → Level2 → Level3

Jede Stufe liefert jeweils:
• eine Klassenvariable        variable_X
• eine Instanzvariable        var_X      (im Konstruktor)
• eine Methode                fun_X()

Da Level3 von Level2 und Level1 erbt, kann ein Level3-Objekt auf ALLES
zugreifen, was in den oberen Stufen definiert wurde.

-----------------------------------------------------------
Erwartete Ausgabe:
-----------------------------------------------------------
100 101 102
200 201 202
300 301 302
"""

class Stufe1:
    variable_1 = 100                                 # Klassenvariable von Stufe1

    def __init__(self):
        self.var_1 = 101                             # Instanzvariable von Stufe1

    def fun_1(self):
        return 102                                   # Methode von Stufe1


class Stufe2(Stufe1):
    variable_2 = 200                                 # Klassenvariable von Stufe2

    def __init__(self):
        super().__init__()                           # Konstruktor von Stufe1 ausführen
        self.var_2 = 201                             # Instanzvariable von Stufe2

    def fun_2(self):
        return 202                                   # Methode von Stufe2


class Stufe3(Stufe2):
    variable_3 = 300                                 # Klassenvariable von Stufe3

    def __init__(self):
        super().__init__()                           # Konstruktor von Stufe2 (und damit Stufe1) ausführen
        self.var_3 = 301                             # Instanzvariable von Stufe3

    def fun_3(self):
        return 302                                   # Methode von Stufe3


objekt = Stufe3()                                    # Objekt der untersten Stufe erzeugen

print(objekt.variable_1, objekt.var_1, objekt.fun_1())# Zugriff über Vererbung auf Stufe1
print(objekt.variable_2, objekt.var_2, objekt.fun_2())# Zugriff über Vererbung auf Stufe2
print(objekt.variable_3, objekt.var_3, objekt.fun_3())# Zugriff direkt aus Stufe3
