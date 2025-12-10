"""
Die rfind()-Methode
Die benannten Ein-, Zwei- und Drei-Parameter-Methoden tun fast dasselbe wie ihre Gegenstücke (die ohne das Präfix r), 
beginnen ihre Suche jedoch am Ende der Zeichenkette, nicht am Anfang (daher das Präfix r für right).
"""

# Demonstrating the rfind() method:
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))




"""
🔍 Was macht rfind()?
-----------------------------------------------------------------
find() sucht von links nach rechts (vom Anfang der Zeichenkette).

rfind() sucht von rechts nach links (vom Ende der Zeichenkette).
-----------------------------------------------------------------
➡️ Beide geben aber den normalen Index zurück – nicht rückwärts!
Nur die Suchrichtung ist anders.

Indexierung der Zeichen:

t a u   t a u   t a u
0 1 2 3 4 5 6 7 8 9 10
-----------------------------------------------------------------
"""

