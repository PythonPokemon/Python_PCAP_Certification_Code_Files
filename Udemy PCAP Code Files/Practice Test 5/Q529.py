
class A:

    x = 0

    def __init__(self, v=0):
        self.y = v
        A.x += v


a = A()
b = A(1)
c = A(2)
print(c.x)  # 3
