
try:
    raise Exception('Hello', 'World')
except Exception as e:
    print(e.args)        # ('Hello', 'World')
    print(type(e.args))  # <class 'tuple'>
