
def func(n):
    s = '*'
    for i in range(n):
        s += s
    yield s
    # return s


for x in func(2):
    print(x, end='')  # ****

print()
print(func(2))        # <generator object func at ...>
print(list(func(2)))  # ['****']

s = '*'
s += s    # s = s + s -> s = '*' + '*' -> '**'
s += s    # s = s + s -> s = '**' + '**' -> '****'
print(s)  # ****
