
class A:
    def __init__(self):
        pass


# a = A(1)  # TypeError: ...
a = A()
print(hasattr(a, 'A'))  # False
