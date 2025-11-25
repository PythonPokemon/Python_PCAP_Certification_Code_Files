
s = '2A'

try:
    n = int(s)
# except: n = 3
except ValueError:
    n = 2
except ArithmeticError:
    n = 1

print(n)
