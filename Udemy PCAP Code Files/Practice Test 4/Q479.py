
print('123' in '1-2-3')        # False
# "123" is not a part of "1-2-3"

print(not 'a' in 'abc')        # False
# "a" is a part of "abc"

print('\n' in """
""")                           # True
# A newline character is a part of every multi-line string.

print(not ('a' not in 'abc'))  # True
print(not False)               # True
# "a" is a part of "abc"
# To times not and it is true again.
