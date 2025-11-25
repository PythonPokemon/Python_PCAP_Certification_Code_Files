
list1 = ['Peter', 'Paul', 'Mary', 'Jane']
list2 = ['Peter', 'Paul', 'Mary', 'Jane']

print(list1 is list2)  # False
print(list1 == list2)  # True

print(id(list1))  # e.g. 140539383900864
print(id(list2))  # e.g. 140539383947452 (a different number)

list1 = list2

print(list1 is list2)  # True
print(list1 == list2)  # True

print(id(list1))  # e.g. 140539652049216
print(id(list2))  # e.g. 140539652049216 (the same number)
