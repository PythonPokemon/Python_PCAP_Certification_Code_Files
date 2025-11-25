
str = 'abcdef'
def fun(s):
    del s[2]  # TypeError: 'str' object doesn't support item deletion
    return s

print(fun(str))
