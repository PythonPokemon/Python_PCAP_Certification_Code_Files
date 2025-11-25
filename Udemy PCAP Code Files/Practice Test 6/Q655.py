
class A:
    # def __init__(self):
    #    pass

    def __str__(self):
        return 'A'


class B(A):
    def __init__(self):
        # super().__init__()
        pass


class C(B):
    def __init__(self):
        # super().__init__()
        pass


b = B()
a = A()
c = C()
print(a, b, c)  # A A A
