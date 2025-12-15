"""
Eigene Ausnahmehierarchie erstellen (Fortsetzung)

Wenn man ein vollständig eigenes Fach- oder Anwendungsgebiet modelliert,
ist es sinnvoll, eine **eigene Ausnahmebasis** zu definieren.

Beispiel: Pizzeria-Simulation

Ziel:
- Eigene Basisausnahme (PizzaFehler)
- Spezialisierte Ausnahmen davon ableiten
- Zusätzliche Kontextinformationen in der Ausnahme speichern

Prüfungsrelevant (PCAP ):
- Eigene Ausnahmen erben von Exception
- Konstruktoren können erweitert werden
- super().__init__() muss korrekt aufgerufen werden
"""

class PizzaFehler(Exception):
    def __init__(self, pizza, meldung):
        super().__init__(meldung)              # Basisklassen-Konstruktor aufrufen
        self.pizza = pizza                     # betroffene Pizza speichern


class ZuVielKaeseFehler(PizzaFehler):
    def __init__(self, pizza, kaese, meldung):
        super().__init__(pizza, meldung)       # PizzaFehler korrekt initialisieren
        self.kaese = kaese                     # zusätzliche Detailinformation


# ---------------------------------------------------------
# Beispielhafte Verwendung
# ---------------------------------------------------------
try:
    raise ZuVielKaeseFehler(
        pizza="Salami",
        kaese=300,
        meldung="Zu viel Käse auf der Pizza"
    )
except ZuVielKaeseFehler as fehler:
    print(fehler)                              # Fehlermeldung
    print("Pizza:", fehler.pizza)              # Zusatzinformation
    print("Käse (g):", fehler.kaese)
