
def func(x):
    if x == 0:
        return 0
    return x + func(x - 1)  # 3 + 2 + 1 + 0


print(func(3))  # 6

# 3 + func(3 - 1)
# 3 + func(2)
# 3 + 2 + func(2 - 1)
# 3 + 2 + func(1)
# 3 + 2 + 1 + func(1 -1)
# 3 + 2 + 1 + func(0)
# 3 + 2 + 1 + 0
# 6

