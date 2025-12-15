"""
Wie Python Eigenschaften und Methoden findet – Fortsetzung
Mehrfache Vererbung & Suchreihenfolge (links → rechts)
------------------------------------------------------

Die Klasse Unterklasse erbt von ZWEI Superklassen:
    • LinkeKlasse
    • RechteKlasse

Beide Superklassen besitzen:
    • eine Klassenvariable mit dem GLEICHEN Namen
    • eine Methode mit dem GLEICHEN Namen

Frage:
Von welcher Klasse stammen Variable und Methode,
wenn sie in beiden Superklassen existieren?

Antwort:
Python durchsucht Superklassen
    → von LINKS nach RECHTS
    → in der Reihenfolge der Klassendeklaration
"""

class LinkeKlasse:
    gemeinsame_variable = "L"                         # gleiche Variable wie in RechteKlasse
    variable_links = "LL"                             # nur in LinkeKlasse vorhanden

    def methode(self):
        return "Left"                                 # gleiche Methode wie in RechteKlasse


class RechteKlasse:
    gemeinsame_variable = "R"                         # gleiche Variable wie in LinkeKlasse
    variable_rechts = "RR"                            # nur in RechteKlasse vorhanden

    def methode(self):
        return "Right"                                # gleiche Methode wie in LinkeKlasse


class Unterklasse(LinkeKlasse, RechteKlasse):
    pass                                              # erbt von LinkeKlasse ZUERST, dann RechteKlasse

"""
🔁 Jetzt die entscheidende Änderung
Nur die Reihenfolge der Superklassen tauschen:

Neue Ausgabe
R LL RR Right
"""
# auskommenzieren zum testen!
# class Unterklasse(RechteKlasse, LinkeKlasse):
#     pass

objekt = Unterklasse()

print(
    objekt.gemeinsame_variable,                       # kommt aus LinkeKlasse
    objekt.variable_links,                            # kommt aus LinkeKlasse
    objekt.variable_rechts,                           # kommt aus RechteKlasse
    objekt.methode()                                  # kommt aus LinkeKlasse
)

"""
🧠 Regel (sehr wichtig & prüfungsrelevant)

Python sucht Eigenschaften & Methoden in folgender Reihenfolge:
    im Objekt selbst
    in den Superklassen
    bei multipler Vererbung: von links nach rechts
    erste gefundene Definition gewinnt
➡️ Die Reihenfolge der Superklassen ist entscheidend.
"""