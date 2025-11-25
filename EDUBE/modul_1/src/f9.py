"""
Ausgewählte Funktionen aus dem Mathematikmodul: Fortsetzung
Eine weitere Gruppe der Funktionen von 's bildet Funktionen, die mit der Exponentiation verbunden sind:math

e → eine Konstante mit einem Wert, der eine Näherung der Eulerschen Zahl (e) ist
exp(x) → den Wert von ex bestimmen;
log(x) → der natürlichen Logarithmus von x
log(x, b) → den Logarithmus von x zur Basis b
log10(x) → der dezimalen Logarithmus von x (genauer als log(x, 10))
log2(x) → den binären Logarithmus von x (genauer als log(x, 2))
"""

from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))


