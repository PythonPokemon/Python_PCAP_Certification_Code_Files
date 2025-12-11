"""
Das Innenleben von Klassen und Objekten – Fortsetzung
-----------------------------------------------------

Ein weiteres eingebautes Attribut jeder Klasse und jedes Objekts lautet:

    __module__

• Es ist eine Zeichenkette.
• Sie enthält den Namen des Moduls, in dem die Klasse definiert wurde.
• Wenn der Code direkt ausgeführt wird (z. B. in einer einzigen .py-Datei),
  dann lautet der Modulname immer: "__main__".

Warum?
Weil "__main__" das virtuelle Modul ist, das für das aktuell laufende
Python-Programm steht.

-----------------------------------------------------------
Erwartete Ausgabe:
-----------------------------------------------------------
__main__
__main__
"""

class Classy:
    pass                                            # einfache Beispielklasse


print(Classy.__module__)                            # Modul der Klasse → "__main__"

obj = Classy()                                      # Objekt erzeugen

print(obj.__module__)                               # auch das Objekt liefert "__main__"
