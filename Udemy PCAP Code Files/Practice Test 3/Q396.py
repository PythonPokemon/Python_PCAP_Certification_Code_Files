
class A:
    value = 1


print(A.value)  # 1

# b = B()  # NameError: name 'B' is not defined


class C:
    __value = 1


print(C.__value)
# AttributeError: type object 'C' has no attribute '__value'
