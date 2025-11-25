
list1 = [3, 7, 23, 42]
list2 = [3, 7, 23, 42]
print(list1 is list2)  # False
print(list1 == list2)  # True

print(id(list1))  # e.g. 140532269484352
print(id(list2))  # e.g. 140532269935296 (a different number)



