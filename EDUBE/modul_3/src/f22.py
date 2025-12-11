"""
Das Innenleben von Klassen und Objekten

Jede Python-Klasse und jedes Python-Objekt besitzt bereits von Haus aus
eine Reihe nützlicher Attribute. Eines davon kennst du bereits gut:
    __dict__

-----------------------------------------------------------
Was ist __dict__?
-----------------------------------------------------------
• Bei OBJEKTEN:
    objekt.__dict__
    → enthält alle Instanzvariablen dieses Objekts
      (also alles, was mit self.xyz angelegt wurde)

• Bei KLASSEN:
    Klassenname.__dict__
    → enthält:
        - alle Methoden
        - alle Klassenvariablen
        - einige interne Python-Strukturen
        - NICHT die Instanzvariablen einzelner Objekte

-----------------------------------------------------------
Was zeigt das Beispiel?
-----------------------------------------------------------
Wir definieren eine Klasse mit:
• einer Klassenvariable:   variable
• einer Instanzvariable:   wert       (im Konstruktor)
• einer normalen Methode:  methode
• einer „versteckten“ Methode: __versteckt

Dann erstellen wir ein Objekt und geben aus:

    1) objekt.__dict__
    2) Klassenname.__dict__

Erwartung:

1) objekt.__dict__:
   → enthält NUR:
       'wert': 2

2) Klassenname.__dict__:
   → enthält:
       'variable': 1
       '__init__': <function ...>
       'methode': <function ...>
       '_Klasse__versteckt': <function ...>   (Name-Mangling!)
       und weitere interne Einträge wie '__module__', '__doc__', ...

-----------------------------------------------------------
Aufgabe zum Verständnis:
-----------------------------------------------------------
• Finde in der Ausgabe der Klasse:
    - die Methoden
    - die Klassenvariable
    - die gemangelte „versteckte“ Methode
• Vergleiche, was im Objekt sichtbar ist:
    → nur Instanzvariablen, keine Methoden.
"""

class Klasse:
    variable = 1                                    # Klassenvariable

    def __init__(self):
        self.wert = 2                               # Instanzvariable

    def methode(self):
        pass                                        # einfache Platzhalter-Methode

    def __versteckt(self):
        pass                                        # „private“ Methode (Name-Mangling greift)


objekt = Klasse()

print(objekt.__dict__)                              # zeigt NUR die Instanzvariablen des Objekts
print(Klasse.__dict__)                              # zeigt Methoden, Klassenvariablen + interne Einträge
