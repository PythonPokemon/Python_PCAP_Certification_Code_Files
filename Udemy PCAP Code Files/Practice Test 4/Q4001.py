
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B):
    pass

class Class_1(C, D): pass

class Class_4(D, A): pass

# class Class_2(B, D): pass
# TypeError: Cannot create a consistent method resolution order (MRO) for bases B, D

# class Class_3(A, C): pass
# TypeError: Cannot create a consistent method resolution order (MRO) for bases A, C
