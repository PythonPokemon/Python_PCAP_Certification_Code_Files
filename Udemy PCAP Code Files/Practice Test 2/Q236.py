
try:
    raise Exception(1, 2, 3)
except Exception as e:
    print(len(e.args))   # 3
    print(type(e.args))  # <class 'tuple'>
    print(e.args)        # (1, 2, 3)

try:
    x = 1 / 0
except Exception as e:
    print(len(e.args))  # 1
    print(e.args)       # ('division by zero',)
