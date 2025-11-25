
# in = 'Hello'  # SyntaxError: invalid syntax
# Does not work because "in" is a python keyword
# for the membership operator:
print(7 in [1, 4, 7, 11])  # True

# Those work because python is case sensitiv
In = 'Hello'
IN = 'Hello'

# This one works because the underscore
# is a valid character for naming variables:
in_ = 'Hello'

import keyword
print(keyword.kwlist)
"""
['False', 'None', 'True', 'and', 'as', 'assert', 'async',
'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
'else', 'except', 'finally', 'for', 'from', 'global', 'if',
'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""
