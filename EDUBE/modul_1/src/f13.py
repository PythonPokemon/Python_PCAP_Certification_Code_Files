"""
Selected functions from the random module: continued

Die Auswahl- und Stichprobenfunktionen

Wie Sie sehen, ist dies kein gutes Werkzeug, um Zahlen in einer Lotterie zu generieren. 
Glücklicherweise gibt es eine bessere Lösung, als eigenen Code zu schreiben, um die Einzigartigkeit der "gezogenen" 
Zahlen zu überprüfen.
"""

from random import randint

for i in range(10):
    print(randint(1, 10), end=',')


# The choice and sample functions
"""
It's a function named in a very suggestive way - choice:

choice(sequence)
sample(sequence, elements_to_choose)
"""

from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

