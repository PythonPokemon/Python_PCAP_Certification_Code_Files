
class A:
    pass
class B:
    pass
class X(A, B):
    pass

bases = X.__bases__
print(type(bases))  # <class 'tuple'>
print(bases)        # (<class '__main__.A'>, <class '__main__.B'>)

base1 = bases[0]()
print(type(base1))           # <class '__main__.A'>
print(isinstance(base1, A))  # True

base2 = bases[1]()
print(type(base2))           # <class '__main__.B'>
print(isinstance(base2, B))  # True

