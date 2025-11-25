
class A:
    def func(self):
        return

class B(A):
    pass

class C(A):
    def func(self):
        return 1

b = B()
c = C()

print(b.func() + c.func())
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
