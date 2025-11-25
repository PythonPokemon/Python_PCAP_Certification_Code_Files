x = 42

def func():
    global x
    print('1. x:', x)
    x = 23
    print('2. x:', x)


func()
print('3. x:', x)

"""
1. x: 42
2. x: 23
3. x: 23
"""