class A:
    __b = 1

    def __init__(self):
        self.c = 1

    def __action(self):
        pass

object = A()

A._A__b -= 1
print(A._A__b )  # 0

object._A__b -= 1
print(object._A__b)  # -1

# A.b -= 1  # AttributeError: type object 'A' has no attribute 'b'

# object__b -= 1  # NameError: name 'object__b' is not defined
