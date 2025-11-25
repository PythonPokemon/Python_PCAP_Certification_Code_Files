
class A:
    def __init__(self):
        self.calc(10)

    def calc(self, i):
        self.i = 3 * i


class B(A):
    def __init__(self):
        super().__init__()
        print('i from B is', self.i)

    def calc(self, i):
        self.i = 2 * i


b = B()  # i from B is 20
