"""
Klassenvariablen

Eine Klassenvariable gehört NICHT zu einem einzelnen Objekt,
sondern zur Klasse selbst. Es existiert genau **eine Kopie**
dieser Variable – egal wie viele Objekte erzeugt werden.

-----------------------------------------------------------
Wichtige Eigenschaften von Klassenvariablen
-----------------------------------------------------------
1) Klassenvariablen existieren bereits, bevor ein Objekt erzeugt wird.
2) Instanzvariablen existieren erst, wenn ein Objekt erzeugt wird.
3) Eine Klassenvariable wird in der Klasse definiert, aber
   außerhalb aller Methoden.
4) Alle Objekte teilen sich denselben Wert der Klassenvariable.
5) Klassenvariablen erscheinen **nicht** im __dict__ der Objekte,
   weil sie nicht Teil des Objekts, sondern der Klasse sind.

-----------------------------------------------------------
Was macht das Beispiel unten?
-----------------------------------------------------------
- Die Klasse besitzt eine Klassenvariable: counter = 0
- Jedes Mal, wenn ein neues Objekt erzeugt wird,
  erhöht der Konstruktor diese Variable um 1.
- Dadurch zählt counter, wie viele Objekte erzeugt wurden.
- Jede Instanz zeigt denselben Wert für counter an.

Erwartete Ausgabe:
{'_BeispielKlasse__erste': 1} 3
{'_BeispielKlasse__erste': 2} 3
{'_BeispielKlasse__erste': 4} 3
"""

class BeispielKlasse:
    zaehler = 0                                      # Klassenvariable (eine gemeinsame Kopie)

    def __init__(self, wert = 1):
        self.__erste = wert                          # private Instanzvariable
        BeispielKlasse.zaehler += 1                  # Klassenvariable erhöhen


obj1 = BeispielKlasse()                              # zaehler = 1
obj2 = BeispielKlasse(2)                             # zaehler = 2
obj3 = BeispielKlasse(4)                             # zaehler = 3

print(obj1.__dict__, obj1.zaehler)                   # Instanzdaten + gemeinsamer Zähler
print(obj2.__dict__, obj2.zaehler)
print(obj3.__dict__, obj3.zaehler)
