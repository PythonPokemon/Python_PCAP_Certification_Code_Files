
class A:
    def __init__(self, x):
        self.__a = x + 1


a = A(0)
# print(a.__a)  # AttributeError ...

# Access by name mangling:
print(a._A__a)  # 1


class B:
    def __init__(self, x):
        self.__b = x + 1

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b


b = B(0)
print(b.b)  # 1
