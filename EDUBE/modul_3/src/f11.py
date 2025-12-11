"""
Instanzvariablen: 

Wir betrachten nun, was passiert, wenn Instanzvariablen mit zwei
Unterstrichen (__) beginnen. Python behandelt solche Variablen als
„privat“, aber das passiert nicht durch echte Sperrung, sondern durch
Name-Mangling („Namensverstümmelung“).

-----------------------------------------------------------
Was bedeutet Name Mangling?
-----------------------------------------------------------
Wenn innerhalb der Klasse eine Variable mit __name erzeugt wird,
macht Python automatisch:

    __name  →  _Klassenname__name

Beispiel:
    self.__erste  wird zu  _BeispielKlasse__erste

Warum? Damit private Variablen nicht versehentlich von außen
überschrieben werden.

-----------------------------------------------------------
Wichtige Hinweise
-----------------------------------------------------------
1) Name-Mangling passiert NUR innerhalb der Klasse.
2) Wenn du außerhalb der Klasse __name definierst, wird NICHT
   umbenannt – die Variable bleibt exakt "__name".
3) Private Variablen sind also nur „versteckt“, nicht wirklich geschützt.
4) Du KANNST trotzdem darauf zugreifen:

       objekt._Klassenname__variable

   (aber OOP-technisch unsauber)

-----------------------------------------------------------
Was zeigt das folgende Beispiel?
-----------------------------------------------------------
obj1 und obj2 erzeugen private Variablen mit Name-Mangling.
obj3 bekommt __dritte außerhalb der Klasse – deshalb *ohne* Mangling.

Die Ausgabe der __dict__-Attribute zeigt die tatsächlichen
Variablennamen im Objekt.
"""

class BeispielKlasse:
    def __init__(self, wert = 1):
        self.__erste = wert                          # → _BeispielKlasse__erste

    def setze_zweite(self, wert = 2):
        self.__zweite = wert                         # → _BeispielKlasse__zweite


obj1 = BeispielKlasse()                              # __erste = 1
obj2 = BeispielKlasse(2)                             # __erste = 2
obj2.setze_zweite(3)                                 # __zweite = 3

obj3 = BeispielKlasse(4)
obj3.__dritte = 5                                     # keine Umbenennung – außerhalb definiert!

print(obj1.__dict__)                                  # zeigt die gemangelten Namen
print(obj2.__dict__)
print(obj3.__dict__)
