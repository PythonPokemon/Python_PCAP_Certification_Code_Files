"""
Die Endswith()-Methode
Die Methode prüft, ob die gegebene Zeichenkette mit dem angegebenen Argument endet, und gibt True oder False zurück, abhängig vom Prüfergebnis.endswith()
"""

# Demonstrating the endswith() method:
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")

print("---------")
# Sie sollten nun in der Lage sein, das Ergebnis des untenstehenden Ausschnitts vorherzusagen:
t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

