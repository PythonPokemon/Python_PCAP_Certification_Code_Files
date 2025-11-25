
# filter even numbers:
print(list(filter(lambda x: x % 2 == 0, [1, 4, 7, 9, 12])))  # [4, 12]
# filter integers:
data = [1.74, 4, '7', (9, 12), 23, 'Hello', [3, 4], 97]


def int_filter(num):
    return type(num) == int


integers = filter(int_filter, data)
for i in integers:
    print(i, end=' ')  # 4 23 97
print()
print(integers)  # <filter object at 0x7fbb6815ed00>
print(hasattr(integers, '__iter__'))   # True
from collections.abc import Iterable
print(isinstance(integers, Iterable))  # True
