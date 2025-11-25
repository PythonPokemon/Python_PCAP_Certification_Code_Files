
w = 7
x = 3
y = 4
z = True
a = w + x * y
b = w + x / z
print(7 + 3 * 4)     # 19
print(7 + (3 * 4))   # 19
print(7 + 12)        # 19
print(a)             # 19
print(7 + 3 / True)  # 10.0
print(7 + 3 / 1)     # 10.0
print(7 + (3 / 1))   # 10.0
print(7 + 3.0)       # 10.0
print(b)             # 10.0
print(a > b)         # True
print(a == b)        # False
print(a <= b)        # False
print(a < b)         # False
if a > b:
    print('TRUE')    # TRUE
else:
    print('FALSE')
