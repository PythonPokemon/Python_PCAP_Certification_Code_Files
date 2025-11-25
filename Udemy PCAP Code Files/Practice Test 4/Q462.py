
try:
    zahl = 100 / 0
except ArithmeticError:
    print('ArithmeticError')  # ArithmeticError
except ZeroDivisionError:
    print('ZeroDivisionError')

try:
    zahl = 100 / 0
except ZeroDivisionError:
    print('ZeroDivisionError')  # ZeroDivisionError
except ArithmeticError:
    print('ArithmeticError')

print(issubclass(ZeroDivisionError, ArithmeticError))  # True
