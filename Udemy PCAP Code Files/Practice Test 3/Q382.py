
def boolean(op):
    return op(False, True)


print(boolean(lambda x, y: x if x else y))  # True

x = False
y = True
if x:
    print(x)
else:
    print(y)  # True
