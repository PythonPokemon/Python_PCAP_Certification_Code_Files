"""
Wie man eine eigene Ausnahme erstellt

Die Python-Ausnahmehierarchie ist erweiterbar.
Eigene Ausnahmen werden erstellt, indem man neue Klassen definiert,
die von bestehenden Ausnahmeklassen erben.

Wichtige Punkte:
- Eigene Ausnahmen sind Klassen
- Sie erben von bestehenden Ausnahmen (z. B. ZeroDivisionError oder Exception)
- Dadurch können sie:
  - wie die Basisausnahme behandelt werden (allgemein)
  - oder gezielt unterschieden werden (spezialisiert)
- Die Reihenfolge der except-Zweige ist entscheidend
"""

class EigeneNullDivision(ZeroDivisionError):
    pass                                           # eigene Ausnahme ohne zusätzliche Logik


def division_ausfuehren(eigene):
    if eigene:
        raise EigeneNullDivision("schlimmere nachricht")   # eigene Ausnahme auslösen
    else:
        raise ZeroDivisionError("schlechte nachricht")     # eingebaute Ausnahme auslösen


for modus in [False, True]:
    try:
        division_ausfuehren(modus)                  # Funktion aufrufen
    except ZeroDivisionError:
        print("Division durch null")                # behandelt beide Ausnahmen gemeinsam


for modus in [False, True]:
    try:
        division_ausfuehren(modus)                  # Funktion erneut aufrufen
    except EigeneNullDivision:
        print("Eigene Division durch null")         # spezielle Behandlung
    except ZeroDivisionError:
        print("Originale Division durch null")      # allgemeine Behandlung
