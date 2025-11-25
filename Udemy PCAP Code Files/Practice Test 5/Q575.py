
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class X(B, C):
    pass


print(X.__bases__)
# (<class '__main__.B'>, <class '__main__.C'>)
