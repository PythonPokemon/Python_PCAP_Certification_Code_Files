
class A:
    x = 23


class B(A):
    x = 42


class C(B):
    pass


c = C()
print(c.x)  # 42
