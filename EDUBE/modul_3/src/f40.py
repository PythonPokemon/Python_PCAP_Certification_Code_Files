"""
Wie man eine Hierarchie von Klassen aufbaut
-------------------------------------------

Dieses Beispiel zeigt einen sehr wichtigen Effekt der Vererbung:
👉 Polymorphie (unterschiedliches Verhalten bei gleicher Methodensignatur)

Es gibt zwei Klassen:
- Basisklasse
- Unterklasse (erbt von Basisklasse)

Beide Klassen definieren dieselbe Methode:
    mache_etwas()

Die Methode wird jedoch NUR EINMAL aufgerufen:
    über die Methode tue_irgendwas()

Entscheidend:
Welche Version von mache_etwas() wird tatsächlich ausgeführt?
"""

class Basisklasse:
    def mache_etwas(self):
        print("mache_etwas aus Basisklasse")           # Standardverhalten

    def tue_irgendwas(self):
        self.mache_etwas()                             # Aufruf der Methode (virtuell!)


class Unterklasse(Basisklasse):
    def mache_etwas(self):
        print("mache_etwas aus Unterklasse")           # Überschreibt Verhalten


# ---------------------------------------------------------
# Objekte erzeugen
# ---------------------------------------------------------
basis_objekt = Basisklasse()
unter_objekt = Unterklasse()

# ---------------------------------------------------------
# Methodenaufrufe
# ---------------------------------------------------------
basis_objekt.tue_irgendwas()                           # nutzt Basisklassen-Version
unter_objekt.tue_irgendwas()                           # nutzt Unterklassen-Version
