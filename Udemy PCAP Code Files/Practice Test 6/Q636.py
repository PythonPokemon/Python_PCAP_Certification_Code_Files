
x = (1, 4, 7, 9, 10, 11)
y = {2: 'A', 4: 'B', 6: 'C', 8: 'D', 10: 'E', 12: 'F'}
res = 1

for z in x:
    if z in y:
        continue
    else:
        print('z:', z)  # 1 -> 7 -> 9 -> 11
        res += z

print(res)  # 29
