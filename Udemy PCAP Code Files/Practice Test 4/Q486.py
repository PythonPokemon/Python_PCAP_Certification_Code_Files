
s = 'three'
e = 0
try:
    e = int(s)
except ArithmeticError:
    e = 1
except:
    e = 2
else:
    e = 3
print(e)  # 2

# print(int('three'))
# ValueError: invalid literal for int() with base 10: 'three'
