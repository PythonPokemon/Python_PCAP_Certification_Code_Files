
print(10 != '1' + '0')       # True
print(10 != '10')            # True
# You can use the not equal to operator with integer and string
# but the values are never the same
# and therefore it will always evaluate to True.

print('9' * 3 > '9' * 9)    # False
print('999' > '999999999')  # False
# '999' is less than '999999999'

# print('9' * 1 < 1 * 2)
# TypeError: '<' not supported between instances of 'str' and 'int'
# You can not use the less than operator with string and integer.

print('Al' * 2 != 2 * 'Al')  # False
print('Al' * 2)  # AlAl
print(2 * 'Al')  # AlAl
# They will both be 'AlAl' and therefore not not equal.
