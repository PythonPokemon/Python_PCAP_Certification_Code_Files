
class A:
    def __init__(self):
        self.x = 1

    def func(self):
        self.x = 10


class B(A):
    def func(self):
        self.x += 1
        return self.x


b = B()
print(b.func())  # 2
