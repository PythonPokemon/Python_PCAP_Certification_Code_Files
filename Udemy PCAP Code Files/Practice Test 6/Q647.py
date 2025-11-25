
# x, y = eval(input('Enter two numbers: '))

x, y = eval('3, 4')              # works
print(type(eval('3, 4')))        # <class 'tuple'>
print(x)  # 3
print(y)  # 4

# x, y = eval('3 4')             # SyntaxError: ...
# x, y = eval('<pre>3 4</pre>')  # SyntaxError: ...
