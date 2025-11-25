
def func(x):
    try:
        x = x / x
    except:
        print('a', end='')
    else:
        print('b', end='')
    finally:
        print('c', end='')


func(1)  # bc
# x = 1 / 1 -> does not raise an exception
# Therefore the else block gets executed -> b
# and the finally block always gets executed -> c

func(0)  # ac
# x = 0 / 0 raises a ZeroDivisionError
# Therefore the except block gets executed -> a
# and the finally block always gets executed -> c
