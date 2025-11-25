
class A:
    def __str__(self):
        return 'A'


class B(A):
    def __str__(self):
        return 'B'


class C(B):
    def __str__(self):
        return 'C'


b = B()
a = A()
c = C()
print(c, b, a)  # C B A
