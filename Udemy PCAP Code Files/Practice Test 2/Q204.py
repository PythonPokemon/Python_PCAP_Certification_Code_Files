
data = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
for i in range(0, 4):
    print(data[i].pop(), end=' ')  # 4 8 12 16

print()
print(list(range(0, 4)))  # [0, 1, 2, 3]

print([1, 2, 3, 4].pop())      # 4
print([5, 6, 7, 8].pop())      # 8
print([9, 10, 11, 12].pop())   # 12
print([13, 14, 15, 16].pop())  # 16
