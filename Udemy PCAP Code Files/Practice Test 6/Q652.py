
for i in range(5, 0, -1):
    print(i, i, i, i, i)

print('-----')

# for i in range(5, 0, None):  # TypeError: ...
#     print(i, i, i, i, i)

print('-----')

# for i in range(5, 0, 0):     # ValueError: ...
#     print(i, i, i, i, i)

print('-----')

for i in range(5, 0, 1):
    print(i, i, i, i, i)

print(list(range(5, 0, 1)))  # []
