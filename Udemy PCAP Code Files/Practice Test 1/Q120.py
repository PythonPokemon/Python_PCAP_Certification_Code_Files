
x = 1
y = 2
# x, y, z = x, x, y
x, y, z = 1, 1, 2  # -> x=1; y=1; z=2
# z, y, z = x, y, z
z, y, z = 1, 1, 2  # -> y=1; z=2
# z will be 1 first and then become 2
# x is still 1
print(x, y, z)     # 1 1 2
