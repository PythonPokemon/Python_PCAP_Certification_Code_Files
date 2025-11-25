
data = {'one': 'two', 'two': 'three', 'three': 'one'}
res = data['three']

for _ in range(len(data)):
    print(res)  # one - two - three
    res = data[res]

print(res)  # one
