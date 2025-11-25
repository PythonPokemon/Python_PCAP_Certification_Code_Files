
# Example 1:
try:
    number = int(input('Please enter a number:\n'))
    result = 42 / number
except ValueError:
    print('You can only use digits.')
except ZeroDivisionError:
    print('Do not enter a zero.')
else:
    print(result)

# Example 2:
try:
    number = int(input('Please enter a number:\n'))
    result = 42 / number
except ValueError:
    print('You can only use digits.')
except ZeroDivisionError:
    print('Do not enter a zero.')
except ZeroDivisionError:
    print('This code is unreachable.')
else:
    print(result)
