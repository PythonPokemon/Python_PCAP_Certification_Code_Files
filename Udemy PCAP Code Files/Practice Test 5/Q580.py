
my_list = [x * x for x in range(5)]
print(my_list)  # [0, 1, 4, 9, 16]
# The same without list comprehension:
my_list = []
for x in range(5):
    my_list.append(x * x)
print(my_list)  # [0, 1, 4, 9, 16]


def fun(lst):
    # del lst[lst[2]]
    del lst[4]
    return lst


print(fun(my_list))  # [0, 1, 4, 9]
