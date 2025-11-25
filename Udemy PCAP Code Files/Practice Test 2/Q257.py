
# A try statement can have a finally clause and an except clause.
try:
    print('try')      # try
except:
    print('except')
finally:
    print('finally')  # finally

# A try statement can have a finally clause without an except clause.
try:
    print('try')      # try
finally:
    print('finally')  # finally

# A try statement can have one or more except clauses.
try:
    # value = input('Please enter a number!')
    value = 'one'
    # value = '0'
    number = 100 / int(value)
except ValueError:
    print('Please enter an integer!')
except ZeroDivisionError:
    print('Please do not enter zero!')
else:
    print('Result:', number)

"""
# A try statement can have one or more finally clauses.
try:
    print('try')
finally:
    print('finally 1')
finally:                # SyntaxError: invalid syntax
    print('finally 2')
"""
