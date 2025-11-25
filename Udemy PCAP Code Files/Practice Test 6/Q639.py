
def get_absolute_integer(num):
    import math
    return math.floor(math.fabs(num))


print(get_absolute_integer(-23.42))  # 23

import math
print(math.floor(4.9))  # 4
print(math.fabs(-4))    # 4.0
print(math.frexp(4))    # (0.5, 3)
print(math.fmod(7, 2))  # 1.0
print(math.ceil(3.1))   # 4
