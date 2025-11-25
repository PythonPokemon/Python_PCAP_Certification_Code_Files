
def func(n):
    s = ''
    for i in range(n):
        s += '*'
        yield s


for x in func(3):
    print(x, end='')  # ******

print()
print(func(3))        # <generator object func at ...>
print(list(func(3)))  # ['*', '**', '***']
