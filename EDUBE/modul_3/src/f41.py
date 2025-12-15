"""
Wie man eine Klassenhierarchie aufbaut – korrektes Beispiel mit Vererbung

Problem:
--------
Zwei Fahrzeugtypen (Kettenfahrzeug und Radfahrzeug) können abbiegen.
Der Ablauf des Abbiegens ist identisch, nur die Art der Lenkung unterscheidet sich.

Lösung:
--------
- Eine Superklasse sammelt den gemeinsamen Ablauf (abbiegen)
- Unterklassen implementieren die konkrete Lenklogik
- Kein doppelter Code
- Polymorphie: gleiche Methode, unterschiedliches Verhalten

"""

import time


class Landfahrzeug:
    def lenken(self, links, aktiv):
        pass                                            # Wird von Unterklassen überschrieben

    def abbiegen(self, links):
        self.lenken(links, True)                        # Lenkung aktivieren
        time.sleep(0.25)                                # Zeit für den Abbiegvorgang
        self.lenken(links, False)                       # Lenkung deaktivieren


class Kettenfahrzeug(Landfahrzeug):
    def lenken(self, links, aktiv):
        if links:
            print("Linke Kette", "STOP" if aktiv else "LAUF")   # linke Kette steuern
        else:
            print("Rechte Kette", "STOP" if aktiv else "LAUF") # rechte Kette steuern


class Radfahrzeug(Landfahrzeug):
    def lenken(self, links, aktiv):
        if aktiv:
            print("Vorderräder nach", "links" if links else "rechts", "drehen")
        else:
            print("Vorderräder geradeaus stellen")


# ---------------------------------------------------------
# Test der Klassenhierarchie
# ---------------------------------------------------------
kettenfahrzeug = Kettenfahrzeug()
radfahrzeug = Radfahrzeug()

print("Kettenfahrzeug biegt links ab:")
kettenfahrzeug.abbiegen(True)

print("\nRadfahrzeug biegt rechts ab:")
radfahrzeug.abbiegen(False)
