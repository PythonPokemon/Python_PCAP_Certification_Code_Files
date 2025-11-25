
class A:
    def __init__(self, x):
        self._a = x + 1
    @property
    def a(self):
        return self._a
    @a.setter
    def a(self, a):
        self._a = a


x = A(23)
print(x.a)   # 24
print(x._a)  # 24 - Pycharm: Access to protected member _a of a class


class B:
    def __init__(self, x):
        self.__b = x + 1
    @property
    def b(self):
        return self.__b
    @b.setter
    def b(self, b):
        self.__b = b


y = B(42)
print(y.b)  # 43
# print(y.__b)  # AttributeError ...
