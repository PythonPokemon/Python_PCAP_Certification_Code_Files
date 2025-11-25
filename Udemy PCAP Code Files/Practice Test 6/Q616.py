
data = [[x for x in range(3)] for y in range(3)]
print(data) # [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
for i in range(3):
    for j in range(3):
        if data[i][j] % 2 != 0:
            print('*')  # * * *
