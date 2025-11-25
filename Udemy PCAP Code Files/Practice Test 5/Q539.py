
# x = input('Enter the first number: ')
# y = input('Enter the second number: ')
x, y = '7', '11'  # Just for convenience

# You cannot concatenate a string and an integer
# print('The Result is ' + (int(x) + int(y)))  # TypeError
# print('The Result is ' + (int(x + y)))       # TypeError

# This works, but you get the wrong result,
# because there is a string concatenation
# before the type casting to integer:
print('The Result is ' + str(int(x + y)))       # 711

print('The Result is ' + str(int(x) + int(y)))  # 18
