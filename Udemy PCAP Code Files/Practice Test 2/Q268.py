
# IndexError:
# e1 = [1, 2][23]  # IndexError ...
print(IndexError.__subclasses__())  # []

# LookupError:
# {1, 2}.remove(3)  # KeyError
print(issubclass(KeyError, LookupError))  # True
print(LookupError.__subclasses__())  # [<class 'IndexError'>, <class 'KeyError'>, ...]

# ArithmeticError:
# e2 = 10 / 0  # ZeroDivisionError ...
print(issubclass(ZeroDivisionError, ArithmeticError))  # True
print(ArithmeticError.__subclasses__())
# [<class 'FloatingPointError'>, <class 'OverflowError'>, <class 'ZeroDivisionError'>]
