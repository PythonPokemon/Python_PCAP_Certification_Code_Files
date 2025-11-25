
try:
    raise Exception('Hello', 'World')
except Exception as err:
    print(err.args)  # ('Hello', 'World')


def f(x):
    try:
        res = 10 // x
    except ZeroDivisionError:
        print('You can not divide by zero!', end='')
    else:
        print('The result is', str(res) + '!', end='')
    finally:
        print(' Always finally!')


f(0)  # You can not divide by zero! Always finally!
f(2)  # The result is 5! Always finally!
