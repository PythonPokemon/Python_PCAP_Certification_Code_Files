
import math


def get_area(r):
    return math.pi * math.pow(r, 2)


print(get_area(2))       # 12.566370614359172
print(math.pi * 2 ** 2)  # 12.566370614359172

print('----------')


def get_area(r):
    return math.pi * math.fmod(r, 2)


print(get_area(2))      # 0.0
print(math.fmod(7, 2))  # 1.0
print(7 % 2)            # 1
print(float(7 % 2))     # 1.0

print('----------')

"""
def get_area(r):
    return math.pi * math.fabs(r, 2)  # TypeError: ...
print(get_area(2))
"""

print(math.fabs(-7.3))  # 7.3
print(math.fabs(-7))    # 7.0
print(abs(-7.3))        # 7.3
print(abs(-7))          # 7
print(float(abs(7)))    # 7.0
