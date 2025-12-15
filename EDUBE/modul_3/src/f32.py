"""
Wie Python Eigenschaften und Methoden findet
-----------------------------------------------------

Jetzt schauen wir uns an, **wie Python bei Vererbung nach Methoden sucht**.

Das ist extrem wichtig, um zu verstehen:
• warum geerbte Methoden funktionieren
• wann Methoden überschrieben werden
• warum Python manchmal Methoden „weiter oben“ findet

-----------------------------------------------------------
Grundidee (vereinfacht):
-----------------------------------------------------------
Wenn du z. B. schreibst:

    print(objekt)

dann sucht Python nach der Methode __str__() in dieser Reihenfolge:

1) In der Klasse des Objekts selbst
2) In der direkten Superklasse
3) In der Superklasse der Superklasse
4) ... bis zur Basisklasse object

Dieser Suchweg heißt:
    Method Resolution Order (MRO)

-----------------------------------------------------------
Beispiel:
-----------------------------------------------------------
• Klasse Super definiert:
    - __init__()
    - __str__()

• Klasse Sub:
    - erbt von Super
    - definiert NUR einen eigenen Konstruktor
    - besitzt KEINE eigene __str__()-Methode

Ergebnis:
→ Sub übernimmt automatisch __str__() von Super

-----------------------------------------------------------
Erwartete Ausgabe:
-----------------------------------------------------------
My name is Andy.
"""

class Super:
    def __init__(self, name):
        self.name = name                              # Name im Objekt speichern

    def __str__(self):
        return "My name is " + self.name + "."        # Textdarstellung des Objekts


class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)                    # Konstruktor der Superklasse aufrufen


objekt = Sub("Andy")                                  # Objekt der Unterklasse erzeugen
print(objekt)                                         # ruft __str__() aus Super auf
