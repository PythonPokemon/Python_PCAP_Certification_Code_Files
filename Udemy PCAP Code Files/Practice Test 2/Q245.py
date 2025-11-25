
num = 1


def func():
    num = 3              # Shadows name 'num' from outer scope
    print(num, end=' ')  # 3


func()

print(num)  # 1
