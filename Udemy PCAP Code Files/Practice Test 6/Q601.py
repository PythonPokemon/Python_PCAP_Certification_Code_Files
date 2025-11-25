
def func(x=2, y=3):
    return x * y


# print(func(y=2, 3))
# SyntaxError: positional argument follows keyword argument
print(func(3, y=2))  # 6
