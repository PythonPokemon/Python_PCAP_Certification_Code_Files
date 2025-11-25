
data = {}
data[1] = 1
data['1'] = 2
data[1.0] = 4

res = 0
for d in data:
    res += data[d]

print(res)                       # 6

print(data)                      # {1: 4, '1': 2}
print({1: 7, 1.0: 23, 1.1: 42})  # {1: 23, 1.1: 42}
