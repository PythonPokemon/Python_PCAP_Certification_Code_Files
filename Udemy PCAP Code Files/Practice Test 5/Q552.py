
try:
    # user_input = input('Please enter a number!')
    user_input = 'one'  # Just for convenience
    # user_input = 1
    num = 100 / int(user_input)
except ValueError:
    print('You need to use digits!')
except:
    print('Error')
else:
    print('Result:', num)

"""
try:
    # user_input = input('Please enter a number!')
    user_input = 'one'  # Just for convenience
    num = 100 / int(user_input)
except:  # SyntaxError: default 'except:' must be last
    print('Error')
except ValueError:
    print('You need to use digits!')
else:
    print('Result:', num)
"""
