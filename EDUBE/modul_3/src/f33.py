"""
Wie Python Eigenschaften und Methoden findet – Fortsetzung
-----------------------------------------------------

Im vorherigen Beispiel haben wir den Konstruktor der Superklasse
so aufgerufen:

    Super.__init__(self, name)

Python bietet dafür eine modernere, sicherere und empfohlene Variante:
    super()

-----------------------------------------------------------
Was macht super()?
-----------------------------------------------------------
• super() liefert ein spezielles Objekt,
  das den Zugriff auf die Superklasse ermöglicht
• der Klassenname muss NICHT explizit genannt werden
• das Argument self wird AUTOMATISCH übergeben
• der Code wird robuster gegenüber Änderungen der Klassenhierarchie

-----------------------------------------------------------
Warum ist super() besser?
-----------------------------------------------------------
• weniger Fehleranfällig
• besser bei Mehrfachvererbung
• besser wartbar
• Standard in modernem Python-Code (PCAP / PCPP!)

-----------------------------------------------------------
Syntax:
-----------------------------------------------------------
super().__init__(argumente)

-----------------------------------------------------------
Wichtig:
-----------------------------------------------------------
super() kann nicht nur Konstruktoren aufrufen,
sondern ALLE Methoden und Attribute der Superklasse.

-----------------------------------------------------------
Erwartete Ausgabe:
-----------------------------------------------------------
My name is Andy.

✅ Merksatz (sehr prüfungsrelevant):
super() ruft Methoden der Superklasse auf,
ohne deren Namen fest zu kodieren.
"""

class Super:
    def __init__(self, name):
        self.name = name                              # Name im Objekt speichern

    def __str__(self):
        return "My name is " + self.name + "."        # menschenlesbare Objekt-Ausgabe


class Sub(Super):
    def __init__(self, name):
        super().__init__(name)                        # Superklassen-Konstruktor aufrufen (empfohlen)


objekt = Sub("Andy")                                  # Objekt der Unterklasse erzeugen
print(objekt)                                         # __str__() wird aus der Superklasse genutzt
