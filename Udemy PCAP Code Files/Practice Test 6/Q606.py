
data = {1: 0, 2: 1, 3: 2, 0: 1}
x = 0

for _ in range(len(data)):
    print(x)  # 0 - 1 - 0 - 1
    x = data[x]

print(x)      # 0
