
class A:
    def __init__(self, x=1):
        self.x = x


class B(A):
    def __init__(self, y=2):
        # super().__init__()
        A.__init__(self)
        # super().__init__(self)
        # e.g. <__main__.B object at 0x7fb220051fa0> 2
        # A.__init__() # TypeError: ...
        self.y = y


b = B()
print(b.x, b.y)  # 1 2
