
class A:

    A = 23

    def __init__(self):
        self.a = 42


print(hasattr(A, 'a'))  # False
print(hasattr(A, 'A'))  # True
