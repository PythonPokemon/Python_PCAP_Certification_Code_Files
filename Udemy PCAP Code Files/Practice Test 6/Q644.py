
"""
try:
    raise Exception
except:           # SyntaxError: default 'except:' must be last
    print('c')
except BaseException:
    print('a')
except Exception:
    print('b')
"""
