
z = 3
y = 7
x = y == z and y > z or z > y and z != y     # False
print(x)                                     # False
print(7 == 3 and 7 > 3 or 3 > 7 and 3 != 7)  # False
print(False and True or False and True)      # False
print((False and True) or (False and True))  # False
print(False or False)                        # False
print(False)                                 # False
