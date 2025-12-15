"""
Eigene Ausnahmen – vollständiges Beispiel mit Vererbung

In diesem Beispiel werden zwei eigene Ausnahmen verwendet:
- PizzaFehler        → allgemeiner Fehler bei der Pizza-Bestellung
- ZuVielKaeseFehler  → spezieller Fehler (Unterklasse von PizzaFehler)

Wichtige Lernziele (PCAP ):
- Eigene Ausnahmen von Exception ableiten
- Ausnahme-Vererbung korrekt nutzen
- Reihenfolge der except-Blöcke ist entscheidend
- Ausnahmeobjekte können Zusatzdaten tragen (Kontext!)
"""

class PizzaFehler(Exception):
    def __init__(self, pizza, meldung):
        super().__init__(meldung)              # Exception korrekt initialisieren
        self.pizza = pizza                     # betroffene Pizza speichern


class ZuVielKaeseFehler(PizzaFehler):
    def __init__(self, pizza, kaese, meldung):
        super().__init__(pizza, meldung)       # PizzaFehler initialisieren
        self.kaese = kaese                     # zusätzliche Detailinformation


def pizza_machen(pizza, kaese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaFehler(pizza, "Pizza nicht auf der Karte")
    if kaese > 100:
        raise ZuVielKaeseFehler(pizza, kaese, "Zu viel Käse")
    print("Pizza fertig!")


# ---------------------------------------------------------
# Testläufe
# ---------------------------------------------------------
bestellungen = [
    ('calzone', 0),
    ('margherita', 110),
    ('mafia', 20)
]

for pz, ks in bestellungen:
    try:
        pizza_machen(pz, ks)
    except ZuVielKaeseFehler as fehler:
        print(fehler, ":", fehler.kaese)       # spezieller Fehler zuerst!
    except PizzaFehler as fehler:
        print(fehler, ":", fehler.pizza)
