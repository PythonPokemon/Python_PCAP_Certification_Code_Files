"""
Der Objektansatz: ein Stapel von Grund auf (Fortsetzung)

Wir erweitern nun die Unterklasse weiter. Die Methode pop() bekommt –
genau wie push() – zusätzliche Funktionalität.

-----------------------------------------------------------
Neue pop()-Methode
-----------------------------------------------------------
Was soll pop() tun?

1) Den obersten Wert vom Stapel holen (Superklassen-Implementierung nutzen!)
2) Diesen Wert von der privaten Summe __summe abziehen
3) Den Wert zurückgeben

Da __stapel_liste privat ist, müssen wir wieder die Methode der
Superklasse verwenden:

    Wert = Superklasse.pop(self)

-----------------------------------------------------------
Die Variable __summe sichtbar machen
-----------------------------------------------------------
__summe ist privat und darf nicht direkt von außen verändert werden.
Um den Wert trotzdem auslesen zu können, definieren wir eine öffentliche
Getter-Methode:

    get_summe()

Diese Methode gibt nur den Wert zurück, schützt ihn aber vor Änderungen.

"""
class Stapel:
    def __init__(self):
        self.__stapel_liste = []                     # private Liste für Stack-Werte

    def push(self, wert):
        self.__stapel_liste.append(wert)             # Wert oben auf den Stapel legen

    def pop(self):
        oberster = self.__stapel_liste[-1]           # obersten Wert holen
        del self.__stapel_liste[-1]                  # obersten Wert entfernen
        return oberster                              # Wert zurückgeben


class AddierStapel(Stapel):
    def __init__(self):
        Stapel.__init__(self)                        # Superklassen-Konstruktor aufrufen
        self.__summe = 0                             # private Summe aller Werte

    def get_summe(self):
        return self.__summe                          # Gesamtsumme zurückgeben

    def push(self, wert):
        self.__summe += wert                         # Wert zur Summe addieren
        Stapel.push(self, wert)                      # normalen Stack-Push ausführen

    def pop(self):
        wert = Stapel.pop(self)                      # Wert vom Stapel holen
        self.__summe -= wert                         # Wert von der Summe abziehen
        return wert                                   # Wert zurückgeben


# ---------------------------------------------------------
# Test des AddierStapels
# ---------------------------------------------------------
stapel = AddierStapel()

for zahl in range(5):
    stapel.push(zahl)                                # Werte 0–4 pushen

print(stapel.get_summe())                            # Erwartet: 10

for _ in range(5):
    print(stapel.pop())                              # Erwartet: 4, 3, 2, 1, 0



# ---------------------------------------------------------
# Test des AddierStapels
# ---------------------------------------------------------
stapel = AddierStapel()

# Werte 0 bis 4 auf den Stack legen
for zahl in range(5):
    stapel.push(zahl)

print(stapel.get_summe())   # Erwartet: 0 + 1 + 2 + 3 + 4 = 10

# Alle Werte wieder herunterholen
for _ in range(5):
    print(stapel.pop())     # Erwartete Ausgabe: 4, 3, 2, 1, 0
