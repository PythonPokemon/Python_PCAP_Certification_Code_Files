
source = [1, 2, 4, 8, 16]
target = [x // 2 for x in source if x < 10]
print(target)     # [0, 1, 2, 4]
print(1 // 2)     # 0
print(target[1])  # 1
