
class A:
    pass


class B(A):
    pass


class C(B):
    pass


print(issubclass(A, C))  # False
print(issubclass(C, A))  # True


class D:
    pass


print(issubclass(C, (A, D)))  # True
