
data = {}


def func(d, key, value):
    d[key] = value


print(func(data, 1, 'Peter'))  # None

print(data)  # {'1': 'Peter'}


