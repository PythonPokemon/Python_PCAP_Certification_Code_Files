
data = [1, 2, 3, 4]
data = list(map(lambda x: 2*x, data))
print(data)  # [2, 4, 6, 8]

print(map(lambda x: 2*x, data))  # <map object at ...>
