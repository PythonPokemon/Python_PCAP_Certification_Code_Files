
my_list = [0 for i in range(1, 3)]
print(my_list)       # [0, 0]
print(len(my_list))  # 2

# The same without list comprehension:
my_list2 = []
for i in range(1, 3):
    my_list2.append(0)
print(my_list)       # [0, 0]
print(len(my_list))  # 2
