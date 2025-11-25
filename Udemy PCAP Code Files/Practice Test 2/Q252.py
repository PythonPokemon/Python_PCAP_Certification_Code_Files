
data = [1, 2, 3, 4, 5, 6]

for i in range(1, 6):  # 1 -> 2 -> 3 -> 4 -> 5
    data[i - 1] = data[i]

print(data)  # [2, 3, 4, 5, 6, 6]

# This is just for output:
for i in range(0, 6):
    print(data[i], end=' ')  # 2 3 4 5 6 6

