
# """
class FirstError(Exception):
    pass
# """


try:
    if '1' != 1:  # True
        raise FirstError
    else:
        print('FirstError has not occured.')
except FirstError:
    print('FirstError has occured.')
else:
    print('None of the above.')

# NameError: name 'FirstError' is not defined
