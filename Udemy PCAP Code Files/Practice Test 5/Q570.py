
my_list = [1, 2, 3]
foo = tuple(map(lambda x: x**x, my_list))
print(foo)  # (1, 4, 27)

my_list = [1, 2, 3]
foo = tuple(map(lambda x: x*x, my_list))
print(foo)  # (1, 4, 9)

my_list = [1, 2, 3]
foo = list(map(lambda x: x**x, my_list))
print(foo)  # [1, 4, 27]

my_list = [1, 2, 3]
foo = list(map(lambda x: x*x, my_list))
print(foo)  # [1, 4, 9]
