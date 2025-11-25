
list1 = [1, 2, 3]
list2 = [10, 100, 1000]
a = map(lambda x, y: x*y, list1, list2)
a = list(a)
print(a)  # [10, 200, 3000]
