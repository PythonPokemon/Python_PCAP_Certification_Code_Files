"""
Klassenvariablen: Fortsetzung

Auch Klassenvariablen können „privat“ gemacht werden, indem man ihnen
zwei Unterstriche (__) voranstellt. Python führt dann sogenanntes
Name-Mangling durch.

-----------------------------------------------------------
Was passiert bei __zaehler ?
-----------------------------------------------------------
Die private Klassenvariable:

    __zaehler

wird intern umbenannt zu:

    _BeispielKlasse__zaehler

Dies verhindert versehentlichen Zugriff von außen, macht die Variable
aber nicht vollständig „unsichtbar“.

-----------------------------------------------------------
Wichtige Punkte
-----------------------------------------------------------
1) Der Konstruktor erhöht die private Klassenvariable bei jeder
   Objekterzeugung.
2) Alle Objekte teilen sich dieselbe Klassenvariable.
3) Der Zugriff ist nur über den gemangelten Namen möglich:
       objekt._BeispielKlasse__zaehler
4) Der Wert erscheint NICHT im __dict__ des Objekts, da er nicht
   zur Instanz gehört.

-----------------------------------------------------------
Erwartete Ausgabe
-----------------------------------------------------------
{'_BeispielKlasse__wert': 1} 3
{'_BeispielKlasse__wert': 2} 3
{'_BeispielKlasse__wert': 4} 3
"""

class BeispielKlasse:
    __zaehler = 0                                     # private Klassenvariable → _BeispielKlasse__zaehler

    def __init__(self, wert = 1):
        self.__wert = wert                            # private Instanzvariable
        BeispielKlasse.__zaehler += 1                 # Klassenvariable erhöhen


objekt1 = BeispielKlasse()                            # zaehler = 1
objekt2 = BeispielKlasse(2)                           # zaehler = 2
objekt3 = BeispielKlasse(4)                           # zaehler = 3

print(objekt1.__dict__, objekt1._BeispielKlasse__zaehler)
print(objekt2.__dict__, objekt2._BeispielKlasse__zaehler)
print(objekt3.__dict__, objekt3._BeispielKlasse__zaehler)
