
class A:
    pass


class B(A):
    pass


class C(B):
    pass


print(issubclass(C, A))  # True
print(issubclass(C, B))  # True
print(issubclass(B, A))  # True
