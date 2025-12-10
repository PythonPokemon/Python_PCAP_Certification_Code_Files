"""

Die Split()-Methode
Die Methode tut, was sie verspricht – sie teilt die Zeichenkette auf und erstellt eine Liste aller erkannten Teilzeichenketten.split()

Die Methode geht davon aus, dass die Teilzeichenketten durch Weißzeichen abgegrenzt sind – die Leerzeichen 
nehmen nicht an der Operation teil und werden nicht in die resultierende Liste kopiert.

Ist die Zeichenkette leer, ist auch die resultierende Liste leer.
"""

# Demonstrating the split() method:
print("phi       chi\npsi".split())     # break \n wird auch ignoriert in der split() methode

# bspl breakline \n ohne split
print("hallo \n oma")


"""
Hinweis: Die umgekehrte Operation kann mit der Methode durchgeführt werden.join()
"""

