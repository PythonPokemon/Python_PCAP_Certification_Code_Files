
fruits1 = ['Apple', 'Pear', 'Banana']
fruits2 = fruits1
fruits3 = fruits1[:]

fruits2[0] = 'Cherry'
fruits3[1] = 'Orange'

res = 0

for i in (fruits1, fruits2, fruits3):
    if i[0] == 'Cherry':
        res += 1
    if i[1] == 'Orange':
        res += 10

print(res)          # 12

print(id(fruits1))  # e.g. 140539383900864
print(id(fruits2))  # e.g. 140539383900864 (the same number)
print(id(fruits3))  # e.g. 140539652049216 (a different number)
