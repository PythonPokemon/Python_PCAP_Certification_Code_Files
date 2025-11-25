
my_tuple = (0, 1, 2, 3, 4, 5, 6)
foo = list(filter(lambda x: x-0 and x-1, my_tuple))
print(foo)  # [2, 3, 4, 5, 6]

my_tuple = (0, 1, 2, 3, 4, 5, 6)
foo = list(filter(lambda x: x == 0 and x == 1, my_tuple))
print(foo)  # []

my_tuple = (0, 1, 2, 3, 4, 5, 6)
foo = tuple(filter(lambda x: x > 1, my_tuple))
print(foo)  # (2, 3, 4, 5, 6)

my_tuple = (0, 1, 2, 3, 4, 5, 6)
foo = tuple(filter(lambda x: x-0 and x-1, my_tuple))
print(foo)  # (2, 3, 4, 5, 6)


print(bool(0 and -1))  # False
print(bool(1 and 0))   # False
print(bool(2 and 1))   # True
print(bool(3 and 2))   # True
print(bool(4 and 3))   # True

