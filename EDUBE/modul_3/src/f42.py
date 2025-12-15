"""
Aufbau einer Klassenhierarchie (Fortsetzung)

Wir führen eine gemeinsame Oberklasse ein, um doppelten Code zu vermeiden
und Polymorphie sauber zu nutzen.

-----------------------------------------------------------
Grundidee
-----------------------------------------------------------
1) Die Oberklasse Fahrzeug definiert den allgemeinen Ablauf des Abbiegens
   in der Methode turn().

2) Die eigentliche Richtungsänderung wird an eine Methode
   change_direction() delegiert.

3) Diese Methode ist in der Oberklasse nur ein Platzhalter
   (abstrakte Methode) und wird in den Unterklassen konkret umgesetzt.

-----------------------------------------------------------
Vorteil
-----------------------------------------------------------
• Der Algorithmus für das Abbiegen (turn) existiert nur EINMAL
• Unterschiedliche Fahrzeugtypen liefern nur ihre jeweilige Umsetzung
• Änderungen am Abbiege-Verhalten müssen nur an einer Stelle erfolgen

→ Klassisches Beispiel für Polymorphie
"""

import time


class Fahrzeug:
    def richtung_aendern(self, links, aktiv):
        pass                                    # abstrakte Methode (wird überschrieben)

    def abbiegen(self, links):
        self.richtung_aendern(links, True)      # Richtungsänderung starten
        time.sleep(0.25)                        # kurze Drehpause
        self.richtung_aendern(links, False)     # Richtungsänderung beenden


class Kettenfahrzeug(Fahrzeug):
    def ketten_steuern(self, links, stoppen):
        pass                                    # konkrete Steuerung der Ketten

    def richtung_aendern(self, links, aktiv):
        self.ketten_steuern(links, aktiv)       # Umsetzung für Kettenfahrzeuge


class Radfahrzeug(Fahrzeug):
    def vorderräder_lenken(self, links, aktiv):
        pass                                    # konkrete Steuerung der Vorderräder

    def richtung_aendern(self, links, aktiv):
        self.vorderräder_lenken(links, aktiv)   # Umsetzung für Radfahrzeuge

