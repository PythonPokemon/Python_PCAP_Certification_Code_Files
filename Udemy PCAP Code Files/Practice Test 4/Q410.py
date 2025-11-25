
data = {'z': 23, 'x': 7, 'y': 42}

for _ in sorted(data):
    print(data[_], end=' ')  # 7 42 23

print()
print(sorted(data))          # ['x', 'y', 'z']
print(data)                  # {'z': 23, 'x': 7, 'y': 42}
