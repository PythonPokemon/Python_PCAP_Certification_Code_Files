
num = 1


def func():
    # num = num + 3  # UnboundLocalError: ...
    print(num)


func()
print(num)

print('----------')

num2 = 1


def func2():
    x = num2 + 3
    print(x)  # 4


func2()

print('----------')

num3 = 1


def func3():
    num3 = 3     # Shadows num3 from outer scope
    print(num3)  # 3


func3()
print(num3)  # 1

