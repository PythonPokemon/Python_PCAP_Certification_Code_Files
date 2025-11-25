
# name = input('Enter your name: ')
name = 'peter'    # peter is all lower case.
# name = 'PETER'  # PETER is all upper case.
# name = 'Peter'  # Peter is mixed case.

if name.lower() == name:
    print(name, 'is all lower case.')
elif name.upper() == name:
    print(name, 'is all upper case.')
else:
    print(name, 'is mixed case.')
