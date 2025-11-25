
v = [1, 2, 3]


def g(a, b, m):
    return m(a, b)


print(g(1, 1, lambda x, y: v[x:y+1]))  # [2]

print([1, 2, 3][1:2])  # [2]


def func(x, y):
    return v[x:y+1]

print(g(1, 1, func))  # [2]



