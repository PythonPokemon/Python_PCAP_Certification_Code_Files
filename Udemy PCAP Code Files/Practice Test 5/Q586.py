
consts = (3.141592, 2.718282)
try:
    print(consts[2])
except Exception as exception:
    print(exception.args)  # ('tuple index out of range',)
else:
    print("('success')")
