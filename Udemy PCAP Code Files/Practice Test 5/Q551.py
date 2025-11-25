
try:
    raise Exception
except BaseException:
    print('1', end='')  # 1
else:
    print('2', end='')
finally:
    print('3')          # 3

print(issubclass(Exception, BaseException))  # True
