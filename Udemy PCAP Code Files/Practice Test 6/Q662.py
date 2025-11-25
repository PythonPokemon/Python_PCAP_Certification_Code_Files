
class A:

    X = 0

    def __init__(self, x='a'):
        A.T = x

    def f(self):
        return 'A'


class B(A):

    X = 0

    def __init__(self, x='b'):
        super().__init__()
        B.T = x

    def f(self):
        print('B')

    def print_stuff(self):
        print(super().X)    # a
        print(self.X)       # b
        print(super().f())  # A
        print(self.f())     # B


b = B()
b.print_stuff()
