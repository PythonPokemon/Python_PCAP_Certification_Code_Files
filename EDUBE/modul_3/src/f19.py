"""
Methoden im Detail: Fortsetzung

Der Parameter „self“ hat zwei zentrale Aufgaben:

-----------------------------------------------------------
1) Zugriff auf Instanzvariablen und Klassenvariablen
-----------------------------------------------------------
• Über self.attribut kannst du auf Instanzvariablen zugreifen.
• Über self.klassenvariable kannst du auf Klassenvariablen zugreifen.
• Falls ein Attribut nicht existiert, wird es zur Laufzeit erzeugt.

Beispiel:
    self.var = 3
→ erstellt eine neue Instanzvariable für dieses Objekt.

-----------------------------------------------------------
Beispiel 1: Zugriff auf Instanz- und Klassenvariablen
-----------------------------------------------------------
Die Klasse besitzt:
• eine Klassenvariable „variable“
• eine Instanzvariable „wert“, die außerhalb der Klasse erzeugt wird

Erwartete Ausgabe:
    2 3
"""

class Klasse:
    variable = 2                                    # Klassenvariable

    def methode(self):
        print(self.variable, self.wert)             # Zugriff auf Klasse + Instanz


objekt = Klasse()
objekt.wert = 3                                     # Instanzvariable erzeugen
objekt.methode()                                     # Ausgabe: 2 3



"""
-----------------------------------------------------------
2) Aufruf anderer Methoden desselben Objekts über self
-----------------------------------------------------------
self wird benutzt, um Methoden der eigenen Klasse aufzurufen.

Beispiel:
    self.andere_methode()

Damit garantiert Python:
• die Methode wird immer am richtigen Objekt ausgeführt
• die Objekt-Identität bleibt erhalten

Erwartete Ausgabe:
    methode
    andere
"""
class KlasseMitMethoden:
    def andere(self):
        print("andere")                               # einfache Ausgabe als Platzhalter-Methode

    def methode(self):
        print("methode")                              # erste Ausgabe der Methode
        self.andere()                                 # Aufruf der anderen Methode über self → gehört zum selben Objekt


obj = KlasseMitMethoden()                             # Objekt der Klasse erstellen
obj.methode()                                         # führt methode() aus → ruft innerhalb andere() auf
