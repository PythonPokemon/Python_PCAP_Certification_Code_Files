"""
Importing a module: continued
"""

import math                 # modul


def sin(x):                 # methoden deklaration
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


pi = 3.14                   # variable

print(sin(pi/2))            # aufruf der funktion(variable / parameter)
print(math.sin(math.pi/2))  # aufruf modul.methode(modul.variable operator parameter)
