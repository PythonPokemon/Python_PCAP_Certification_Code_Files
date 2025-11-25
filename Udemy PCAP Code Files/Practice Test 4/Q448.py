
# """
data = ['peter', 'paul', 'mary']
for d in data:
    data.append(d.upper())
print(data)
# """

# This would work:
data = ['peter', 'paul', 'mary']
res = []
for d in data:
    res.append(d.upper())
print(res)  # ['PETER', 'PAUL', 'MARY']
