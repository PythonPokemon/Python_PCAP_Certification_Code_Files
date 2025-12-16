# objekt refenz

list1 = [0, 1, 2, 3]
list2 = list1
list3 = list2[0:2]

print("list1 inhalt: ", list1, "→ id =", id(list1))
print("list2 inhalt: ", list2, "→ id =", id(list2))
print("list3 inhalt: ",list3, "→ id =", id(list3))

print(list1 == list2)
print(list2 == list3)