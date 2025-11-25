
import random
a = random.randint(0, 100)
b = random.randrange(10, 100, 3)
c = random.choice((0, 100, 3))
print(a, b, c)  # e.g. 6 82 0
print(random.randint(0, 100))        # e.g. 0, 1, 2, ... 98, 99, 100
print(random.randrange(10, 100, 3))  # e.g. 10, 13, 16, ... 91, 94, 97
print(random.choice((0, 100, 3)))    # e.g. 0, 100, 3
