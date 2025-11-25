
print((lambda x: x + 1)(7))  # 8

print((lambda x: None)("Whatever"))  # None

# print((lambda x = x + 1)(7))
# SyntaxError: invalid syntax

# print((lambda(x): return x + 1)(7))
# SyntaxError: invalid syntax
