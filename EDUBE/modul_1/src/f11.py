"""
Gibt es echte Zufälligkeit bei Computern?
Ein weiteres erwähnenswertes Modul ist das mit dem Namen .random

Es bietet einige Mechanismen, die es ermöglichen, mit Pseudozufallszahlen zu arbeiten.
------------------------------------------------------------------------------------------------------------------------
Ein Zufallszahlengenerator nimmt einen Wert, der als Seed bezeichnet wird, behandelt ihn als Eingabewert, 
berechnet darauf basierend eine "Zufallszahl" (die Methode hängt von einem gewählten Algorithmus ab) 
und erzeugt einen neuen Seed-Wert.
------------------------------------------------------------------------------------------------------------------------
Der Zufallsfaktor des Prozesses kann ergänzt werden, indem der Seed mit einer Zahl aus der aktuellen Zeit gesetzt wird – 
so wird sichergestellt, dass jeder Programmstart mit einem anderen Startwert startet 
(daher werden unterschiedliche Zufallszahlen verwendet).
------------------------------------------------------------------------------------------------------------------------
Die Seed-Funktion

Die Funktion kann den Seed des Generators direkt setzen. Wir zeigen Ihnen zwei seiner Varianten:seed()

seed() - setzt den Seed mit der aktuellen Zeit;
seed(int_value) - setzt den Seed mit dem ganzzahligen Wert .int_value
"""

# variante 1:
from random import random, seed

seed(0)

for i in range(5):
    print(random())



