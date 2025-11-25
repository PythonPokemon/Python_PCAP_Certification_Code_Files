
class A:
    def __init__(self):
        self.i = 0
        self.calc(10)
        print('i from A is', self.i)

    def calc(self, i):
        self.i = 2 * i


class B(A):
    def __init__(self):
        super().__init__()

    def calc(self, i):
        self.i = 3 * i


b = B()  # i from A is 30

