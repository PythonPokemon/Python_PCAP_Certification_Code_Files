
"""
try:
    raise Exception
except:
    print("c")
except BaseException:
    print("a")
except Exception:
    print("b")
"""
# SyntaxError: default 'except:' must be last

# This still does not make much sense,
# but there would be no syntax error.
try:
    raise Exception
except BaseException:
    print("a")         # a
except Exception:
    print("b")
except:
    print("c")
