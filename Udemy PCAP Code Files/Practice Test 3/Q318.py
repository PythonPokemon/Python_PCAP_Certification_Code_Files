
class A:
    def __init__(self):
        self.i = 1

    def func(self):
        self.i = 10


class B(A):
    def func(self):
        self.i += 1
        return self.i


b = B()
print(b.func())  # 2
