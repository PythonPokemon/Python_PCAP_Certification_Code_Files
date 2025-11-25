class A:

    A = 1

    def __init__(self, x=2):
        self.x = x + A.A
        A.A += 1

    def set(self, x):
        self.x += x
        A.A += 1


a = A()
a.set(2)
print(a.x)  # 5
