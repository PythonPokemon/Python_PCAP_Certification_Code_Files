"""
Operations on strings: the index() method
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Die Methode (es ist eine Methode, keine Funktion) sucht die Sequenz von Anfang an, um das erste Element des in ihrem Argument angegebenen Wertes zu finden.index()

Hinweis: Das gesuchte Element muss in der Sequenz auftreten – sein Fehlen führt zu einer ValueError-Ausnahme.

Die Methode gibt den Index des ersten Vorkommens des Arguments zurück (was bedeutet, dass das niedrigstmögliche Ergebnis 0 ist, 
während das höchste die Länge des Arguments mit 1 verringert ist).
"""

# Demonstrating the index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))