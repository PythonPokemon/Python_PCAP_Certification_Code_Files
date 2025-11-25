
list1 = [1, 3]
list2 = list1
list1[0] = 4
print(list2)  # [4, 3]
print(id(list1))  # e.g. 140539383947452
print(id(list2))  # e.g. 140539383947452 (the same number)
