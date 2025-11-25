
class A:
    def __init__(self):
        self.a = 1


class B(A):
    def __init__(self):
        A.__init__(self)
        # __init__()     # NameError
        # A.__init__()   # TypeError
        # A.__init__(1)  # AttributeError ...
        self.b = 2


b = B()
