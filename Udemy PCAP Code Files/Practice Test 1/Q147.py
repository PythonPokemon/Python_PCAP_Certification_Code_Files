
x = [0, 1, 2]
x.insert(0, 1)
print(x)       # [1, 0, 1, 2]
del x[1]
print(x)       # [1, 1, 2]
print(sum(x))  # 4
