
consts = (3.141592, 2.718282)
try:
    print(consts.index(314e-2))
    # print(consts.index(3.141592))
except Exception as exception:
    print(exception.args)  # ('tuple.index(x): x not in tuple',)
else:
    print("('success')")

print(314e-2)  # 3.14
# print(consts.index(314e-2))  # ValueError: ...
