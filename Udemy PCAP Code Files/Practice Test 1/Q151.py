
class A:
    pass


obj = A()

print(isinstance(obj, A))    # True
# print(obj.isinstance(A))   # AttributeError: ...
# print(A.isinstance(obj))   # AttributeError: ...
# print(isinstance(A, obj))  # TypeError: ...


class B:
    pass


class C:
    pass


print(isinstance(obj, (A, B, C)))  # True
