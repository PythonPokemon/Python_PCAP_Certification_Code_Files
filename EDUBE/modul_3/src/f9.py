"""
Der Objektansatz: ein Stapel von Grund auf (Fortsetzung)

Wir erweitern nun die Unterklasse weiter, indem wir die Methoden push()
und pop() überschreiben („override“). Die Namen bleiben gleich,
aber die Funktionsweise wird erweitert.

Wichtig:
• Die Superklasse besitzt push() und pop()
• Wir wollen in der Unterklasse **zusätzliche Arbeit** erledigen:
    - push(wert):  Wert zur Summe __summe addieren + normalen Stack-Push ausführen
    - pop():       Wert vom Stack holen + von der Summe abziehen

Das bedeutet:
Wir ersetzen die Implementierung, aber NICHT den Methodennamen.
Die Schnittstelle bleibt identisch → das nennt man „Überschreiben“.

-----------------------------------------------------------
push() in der Unterklasse
-----------------------------------------------------------
Was soll push() tun?

1) Den Wert in der Variablen __summe mitzählen
2) Den Wert auf den Stapel legen (Superklasse verwendet __stapel_liste)

Hinweis:
Wir dürfen NICHT direkt auf __stapel_liste zugreifen (private Variable!)
Daher müssen wir den push() der Superklasse aufrufen:

    Superklasse.push(self, wert)

Beachte zwei Dinge:
• Wir müssen den Klassennamen explizit angeben (Stapel.push)
• Wir müssen self manuell übergeben (innerhalb einer Klasse notwendig)

Das ist die korrekte Definition der überschriebenen Methode:
"""
class Stapel:
    def __init__(self):
        self.__stapel_liste = []

    def push(self, wert):
        self.__stapel_liste.append(wert)

    def pop(self):
        oberster = self.__stapel_liste[-1]
        del self.__stapel_liste[-1]
        return oberster


class AddierStapel(Stapel):
    def __init__(self):
        # Konstruktor der Superklasse muss explizit aufgerufen werden!
        Stapel.__init__(self)
        self.__summe = 0

    def push(self, wert):
        """
        Neue push()-Implementierung:
        1. Wert zur Summe hinzufügen
        2. push() der Superklasse aufrufen (legt Wert auf den Stapel)
        """
        self.__summe += wert
        Stapel.push(self, wert)
