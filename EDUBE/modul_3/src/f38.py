"""
Wie Python Eigenschaften und Methoden findet – Fortsetzung
Überschreiben (Overriding) in der Vererbung
-----------------------------------------------------

Wenn eine Unterklasse eine Eigenschaft oder Methode mit
dem GLEICHEN Namen definiert wie ihre Superklasse, dann
wird die ältere Definition überschrieben.

Wichtig:
• Es existieren NICHT zwei Versionen gleichzeitig
• Die unterste Klasse in der Vererbungskette gewinnt
• Python sucht von UNTEN nach OBEN und nimmt den
  ERSTEN passenden Treffer

-----------------------------------------------------------
Beispiel:
-----------------------------------------------------------
• StufeEins definiert:
    - klassen_variable = 100
    - methode() → 101

• StufeZwei erbt von StufeEins und überschreibt:
    - klassen_variable = 200
    - methode() → 201

• StufeDrei erbt von StufeZwei und fügt nichts hinzu

Ein Objekt von StufeDrei nutzt daher automatisch
die überschriebenen Definitionen aus StufeZwei.

-----------------------------------------------------------
Erwartete Ausgabe:
-----------------------------------------------------------
200 201

✔ Merksatz (prüfungsrelevant, aber ohne Meta-Gelaber)

Python sucht Eigenschaften und Methoden von unten nach oben
und verwendet die erste gefundene Definition.
"""

class StufeEins:
    klassen_variable = 100                           # Klassenvariable aus StufeEins

    def methode(self):
        return 101                                   # Methode aus StufeEins


class StufeZwei(StufeEins):
    klassen_variable = 200                           # überschreibt klassen_variable aus StufeEins

    def methode(self):
        return 201                                   # überschreibt methode() aus StufeEins


class StufeDrei(StufeZwei):
    pass                                              # erbt alles von StufeZwei


objekt = StufeDrei()                                 # Objekt der untersten Klasse erzeugen

print(objekt.klassen_variable, objekt.methode())     # nutzt StufeZwei → 200 201
