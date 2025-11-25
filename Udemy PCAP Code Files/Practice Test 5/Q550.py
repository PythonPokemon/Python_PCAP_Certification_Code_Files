
def func():
    try:
        return 1
    finally:
        return 2


res = func()
print(res)  # 2


# For comparison:
def func2():
    try:
        print(1)  # 1
    finally:
        print(2)  # 2


func2()
