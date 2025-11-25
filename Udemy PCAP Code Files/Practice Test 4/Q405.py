
def func1(param):
    return param      # 8 -> 8


def func2(param):
    return param * 2  # 4 * 2 -> 8


def func3(param):
    return param + 3  # 1 + 3 -> 4


print(func1(func2(func3(1))))  # 8
