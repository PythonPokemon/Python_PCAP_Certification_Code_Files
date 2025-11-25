
# First execute the following to create the needed file:
with open('data.txt', 'w') as f:
    f.write('Hello')

with open('data.txt', 'r') as f:
    print(f.read())  # Hello

with open('data.txt', 'r+') as f:
    print(f.read())  # Hello

"""
with open('data.txt', 'a') as f:
    print(f.read())  # io.UnsupportedOperation: not readable
"""

"""
with open('data.txt', 'w') as f:
    print(f.read())  # io.UnsupportedOperation: not readable
"""
