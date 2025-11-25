
def f(a, b):
    return b(b)  # TypeError: 'int' object is not callable
    # return a(b)


print(f(lambda x: x + 1, 0))
