
data = [[x for x in range(y)] for y in range(3)]
print(data)         # [[], [0], [0, 1]]

for d in data:
    print('d:', d)  # [] -> [0] -> [0, 1]
    if len(d) < 2:
        print('*')  # * *
