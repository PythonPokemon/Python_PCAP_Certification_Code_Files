
print(10 == '1' + '0')     # False
# You can compare a string and an integer
# with the equal to operator (==)
# or the not equal to operator(!=).
# But it will always retruns False.

print('Al' * 2 <= 'Alan')  # True
# 'AlAl' is less than 'Alan' because 'A' is less than 'a'.

print('9' * 3 < '9' * 9)   # True
# True, because '999' is less than '999999999'.

print('9' * 1 <= 1 * 2)
# TypeError: '<=' not supported
# between instances of 'str' and 'int'
# You cannot compare a string and an integer with any other than
# the equal to operator (==) or the not equal to operator(!=).
