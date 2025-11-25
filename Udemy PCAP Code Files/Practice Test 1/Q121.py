
def func(x):
    return 1 if x % 2 != 0 else 2


print(func(func(1)))  # 1

print(1 % 2)          # 1
print(1 % 2 != 0)     # True
