
class A:

    def __init__(self, x=1):
        self.x = x

    def set(self, x):
        self.x = x + 3
        # return x
        return self.x


a = A()
print(a.set(a.x + 1))  # 2
