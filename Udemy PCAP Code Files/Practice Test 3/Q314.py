
def func(x, y=2):
    num = 1
    for i in range(y):
        num = num * x
    return num


print(func(4))         # 16 (4 * 4)
print(func(4, 4))      # 256 (4 * 4 * 4 * 4)

import math
print(math.pow(4, 2))  # 16.0
# print(math.pow(4))   # TypeError: pow expected 2 arguments, got 1
