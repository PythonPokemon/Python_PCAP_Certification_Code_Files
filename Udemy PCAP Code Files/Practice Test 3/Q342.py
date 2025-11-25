
x = 0
y = 1
print(x, y)   # 0 1
x = x ^ y
print(x, y)   # 1 1
y = x ^ y
print(x, y)   # 1 0
y = x ^ y
print(x, y)   # 1 1

print(1 ^ 1)  # 0
print(1 ^ 0)  # 1
print(0 ^ 1)  # 1
print(0 ^ 0)  # 0
