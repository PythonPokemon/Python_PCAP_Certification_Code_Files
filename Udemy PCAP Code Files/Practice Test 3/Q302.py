
z = 2
y = 1
x = y < z or z > y and y > z or z < y
print(x)                                  # True
print(y < z or z > y and y > z or z < y)  # True
print(1 < 2 or 2 > 1 and 1 > 2 or 2 < 1)  # True
print(True or True and False or False)    # True
print(True or (True and False) or False)  # True
print(True or False or False)             # True
print((True or False) or False)           # True
print(True or False)                      # True
print(True)                               # True
