"""
Das Innenleben von Klassen und Objekten – Fortsetzung
-----------------------------------------------------

Das Attribut __bases__ ist ein Tupel.
Es enthält die direkten Superklassen einer Klasse – also die Klassen,
von denen diese Klasse unmittelbar erbt.

Wichtig:

• __bases__ steht NUR Klassen zur Verfügung – nicht Objekten.
• Jedes Element im Tupel ist eine Klasse, kein Name.
• Die Reihenfolge entspricht genau der Reihenfolge in der Klassendefinition.
• Wenn eine Klasse KEINE Superklasse angibt, erbt sie automatisch von "object".

Beispiel:
class Sub(SuperOne, SuperTwo):
    pass

Dann lautet:
Sub.__bases__ → (SuperOne, SuperTwo)

Wir verwenden eine Hilfsfunktion printBasen(), um das Tupel lesbar auszugeben.

Erwartete Ausgabe:
( object )
( object )
( SuperOne SuperTwo )
"""

class SuperOne:
    pass                                           # einfache Superklasse ohne eigenen Inhalt


class SuperTwo:
    pass                                           # zweite Superklasse


class Sub(SuperOne, SuperTwo):
    pass                                           # erbt von beiden Klassen


def printBasen(klasse):
    print("( ", end="")                             # Formatierung
    for basis in klasse.__bases__:                  # durch alle direkten Superklassen iterieren
        print(basis.__name__, end=" ")              # Klassennamen ausgeben
    print(")")                                      # Abschluss der Zeile


printBasen(SuperOne)                                # erwartet: ( object )
printBasen(SuperTwo)                                # erwartet: ( object )
printBasen(Sub)                                     # erwartet: ( SuperOne SuperTwo )
