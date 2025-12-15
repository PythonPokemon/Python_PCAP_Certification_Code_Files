"""
Vererbung: issubclass()

Python bietet die Funktion issubclass(), um zu prüfen, ob eine Klasse
eine Unterklasse (Subklasse) einer anderen Klasse ist.

Syntax:
    issubclass(KlasseA, KlasseB)

Bedeutung:
• True  → wenn KlasseA eine Unterklasse von KlasseB ist
• False → sonst

-----------------------------------------------------------
Wichtige Beobachtung (PCAP/PCPP-relevant):
-----------------------------------------------------------
Jede Klasse gilt als Unterklasse von sich selbst:

    issubclass(Klasse, Klasse)  → True

-----------------------------------------------------------
Beispiel (3-stufige Vererbung)
-----------------------------------------------------------
Vehicle → LandVehicle → TrackedVehicle

Wir prüfen alle möglichen geordneten Paare (cls1, cls2) und geben aus,
ob cls1 eine Unterklasse von cls2 ist.

Erwartete Ausgabe (als Tabelle gedacht):
True   False  False
True   True   False
True   True   True

Erklärung:
• Vehicle ist Unterklasse von Vehicle (True), aber nicht von LandVehicle (False)
• LandVehicle ist Unterklasse von Vehicle (True) und von sich selbst (True)
• TrackedVehicle ist Unterklasse von LandVehicle (True) und Vehicle (True) und sich selbst (True)
"""

class Fahrzeug:
    pass                                            # Oberklasse (Basis)


class LandFahrzeug(Fahrzeug):
    pass                                            # erbt von Fahrzeug


class KettenFahrzeug(LandFahrzeug):
    pass                                            # erbt von LandFahrzeug (und damit auch von Fahrzeug)


for klasse_1 in [Fahrzeug, LandFahrzeug, KettenFahrzeug]:          # jede Klasse einmal als „zu prüfende Klasse“
    for klasse_2 in [Fahrzeug, LandFahrzeug, KettenFahrzeug]:      # jede Klasse einmal als mögliche Superklasse
        print(issubclass(klasse_1, klasse_2), end="\t")            # True/False ausgeben, tab-getrennt
    print()                                                        # Zeilenumbruch nach jeder Reihe
