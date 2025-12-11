"""
Der Objektansatz: ein Stapel von Grund auf (Fortsetzung)

Wir erweitern unser Stack-Konzept:
Wir möchten eine NEUE Klasse bauen, die ALLE Funktionen des bisherigen
Stacks erbt, aber zusätzlich den Gesamtwert aller gespeicherten Elemente
mitführen kann.

Wichtig:
• Die bestehende Klasse Stapel soll NICHT geändert werden.
• Stattdessen erstellen wir eine Unterklasse (Subklasse).
• Die neue Klasse soll push() und pop() erweitern:
    - push(wert) → Wert auf den Stapel legen + zur Summe addieren
    - pop()      → Wert vom Stapel nehmen + von der Summe abziehen

-----------------------------------------------------------
1) Erstellen einer Unterklasse
-----------------------------------------------------------
Die Syntax lautet:

    class NeueKlasse(AlteKlasse):
        pass

Damit erbt die neue Klasse *alle* Methoden und Attribute der Superklasse.

Beispiel:
    class AddierStapel(Stapel):
        pass

Diese Klasse ist NICHT leer — sie erbt die komplette Funktionalität
ihrer Superklasse.

-----------------------------------------------------------
2) Neue private Variable für die Summe
-----------------------------------------------------------
Wir fügen in der Unterklasse eine neue Eigenschaft hinzu:

    self.__summe = 0

Da es eine private Variable ist, beginnt sie mit __.

-----------------------------------------------------------
3) Der Konstruktor der Unterklasse
-----------------------------------------------------------
Jetzt kommt der entscheidende Punkt:

Python ruft NICHT automatisch den Konstruktor der Superklasse auf!

Das bedeutet:
Wenn wir Stack.__init__(self) NICHT aufrufen,
wird die interne Liste __stapel_liste NICHT erstellt.
Der Stack würde dann nicht funktionieren.

Darum müssen wir explizit den Konstruktor der Superklasse aufrufen:

    Stapel.__init__(self)

Erst danach darf die Unterklasse eigene Attribute anlegen.

-----------------------------------------------------------
4) Syntax des Superklassen-Konstruktors
-----------------------------------------------------------
Innerhalb der Klasse schreibt man:

    Superklasse.__init__(self)

• self muss angegeben werden — innerhalb der Klasse IMMER verpflichtend.
• Von außen wäre das anders (Python übergibt self automatisch).

-----------------------------------------------------------
Hier ist die fertige Unterklasse:
"""
class Stapel:
    def __init__(self):
        self.__stapel_liste = []

    def push(self, wert):
        self.__stapel_liste.append(wert)

    def pop(self):
        oberster_wert = self.__stapel_liste[-1]
        del self.__stapel_liste[-1]
        return oberster_wert


class AddierStapel(Stapel):
    def __init__(self):
        # Konstruktor der Superklasse aufrufen → erzeugt __stapel_liste
        Stapel.__init__(self)
        # Neue private Eigenschaft für die Summe
        self.__summe = 0
