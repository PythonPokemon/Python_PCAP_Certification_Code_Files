
# True = 3  # SyntaxError: cannot assign to True
# Those three work, because Python is case sensitive:
true = 7
tRUE = 23
TRUE = 42
print(true, tRUE, TRUE)  # 7 23 42
