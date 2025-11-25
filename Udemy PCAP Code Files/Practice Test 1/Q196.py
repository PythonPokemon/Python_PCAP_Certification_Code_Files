
class A:
    private_data = 1
    privatedata__ = 1
    _privatedata_ = 1
    __privatedata = 1


print(A.private_data)     # 1
print(A.privatedata__)    # 1
print(A._privatedata_)    # 1
# print(A.__privatedata)  # AttributeError: ...
