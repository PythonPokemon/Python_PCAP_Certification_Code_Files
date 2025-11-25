
def func1(a):
    return a ** a


def func2(a):
    # return func1(a) * func1(a)
    # return (a ** a) * (a ** a)
    # return (2 ** 2) * (2 ** 2)
    # return 4 * 4
    return 16


print(func2(2))  # 16
