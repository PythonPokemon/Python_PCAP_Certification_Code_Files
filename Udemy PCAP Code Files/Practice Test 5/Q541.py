
data = ['Peter', 'Paul', 'Mary', 'Jane']
res = 0
for i in ('Peter', 'Steve', 'Jane'):
    if i not in data:
        res += 100
print(res)  # 100

# ----------------------

res = 0
for i in ('Peter', 'Steve', 'Jane'):
    if i in data:
        res += 50
print(res)  # 100

# ----------------------

res = 0
for i in ('Peter', 'Steve', 'Jane'):
    if i in data:
        res += 100
print(res)  # 200

# ----------------------

res = 0
for i in ('Peter', 'Steve', 'Jane'):
    if i not in data:
        res += 50
print(res)  # 50
