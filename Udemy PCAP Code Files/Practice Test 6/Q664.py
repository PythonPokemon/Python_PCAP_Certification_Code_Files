
import math
try:
    print(math.pow(2))
except TypeError:
    print('A')
else:
    print('B')

# math.pow(2)
# TypeError: pow expected 2 arguments, got 1

print(math.pow(2, 8))  # 256.0
