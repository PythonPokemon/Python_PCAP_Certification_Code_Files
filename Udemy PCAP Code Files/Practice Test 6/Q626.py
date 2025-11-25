
class A:

    # a = 0

    def __init__(self):
        pass


a = A(1)
# TypeError: __init__() takes 1 positional argument but 2 were given
# a = A()
print(hasattr(A, 'a'))   # False
print(isinstance(a, A))  # True
