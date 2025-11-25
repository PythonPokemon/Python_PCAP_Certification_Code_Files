
data = [[42, 17, 23, 13], [11, 9, 3, 7]]
res = data[0][0]
print(res)  # 42
for da in data:
    for d in da:
        if res > d:
            print('d: ', d)  # 17 -> 13 -> 11 -> 9 -> 3
            res = d
print(res)  # 3
