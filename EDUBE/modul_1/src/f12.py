"""
Selected functions from the random module: continued
The randrange and randint functions

If you want integer random values, one of the following functions would fit better:

randrange(end)
randrange(beg, end)
randrange(beg, end, step)
randint(left, right)
"""

from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))
