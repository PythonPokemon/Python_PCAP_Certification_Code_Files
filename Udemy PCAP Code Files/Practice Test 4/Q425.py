class A:
    def __str__(self):
        return 'A'


class B(A):
    def __str__(self):
        return 'B'


class C(B):
    pass


c = C()
print(c)  # B
