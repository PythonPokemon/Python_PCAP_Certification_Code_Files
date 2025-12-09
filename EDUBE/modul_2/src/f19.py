"""
Die find()-Methode
Die Methode ist ähnlich wie , den du bereits kennst – sie sucht nach einer Teilzeichenkette und gibt den Index des ersten Vorkommens 
dieser Teilzeichenkette zurück, aber:find()index()
"""

# Demonstrating the find() method:
print("Eta".find("ta"))
print("Eta".find("mma"))

# Hinweis: Verwenden Sie nicht, wenn Sie nur prüfen wollen, ob ein einzelnes Zeichen in einer Zeichenkette vorkommt – der Operator ist deutlich schneller.find()in
t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))

# Das zweite Argument spezifiziert den Index, bei dem die Suche gestartet wird (er muss nicht in die Zeichenkette passen).
print('kappa'.find('a', 2))

"""
Es gibt auch eine Drei-Parameter-Mutation der find()-Methode – das dritte Argument zeigt auf den ersten Index, 
der bei der Suche nicht berücksichtigt wird (er ist tatsächlich das obere Limit der Suche).
"""
print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))

