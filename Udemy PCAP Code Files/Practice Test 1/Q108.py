
d = {}
print(d)  # {}
d[1] = 1
print(d)  # {1: 1}
d['1'] = 2
print(d)  # {1: 1, '1': 2}
d[1] += 1
print(d)  # {1: 2, '1': 2}

sum = 0
for k in d:
    sum += d[k]
    print("key: ", k, " - value: ", d[k])
    # key:  1  - value:  2
print(sum)  # 4

sum = 0
for k in d.keys():
    sum += d[k]
    print("key: ", k, " - value: ", d[k])
    # key:  1  - value:  2
print(sum)  # 4
