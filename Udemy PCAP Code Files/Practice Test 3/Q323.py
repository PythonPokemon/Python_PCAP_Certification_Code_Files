
data = [(0, 1), (1, 2), (2, 3)]
res = sum(i for j, i in data)
print(res)  # 6

print(i for j, i in data)    # <generator object <genexpr> at ...>
print(i for (j, i) in data)    # <generator object <genexpr> at ...>
print([i for j, i in data])  # [1, 2, 3]
print([i for (j, i) in data])  # [1, 2, 3]
