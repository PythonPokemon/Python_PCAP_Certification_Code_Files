
# This works:
file = open('data.txt', 'w+')
file.write('Hello')
file.seek(0)
data = file.read()
print(data)  # Hello
file.close()

# This would not create the not existing file:
# To test it, delete the file before running it.
# open('data.txt', 'r+')  # FileNotFoundError: ...

"""
# This only opens for reading:
file = open('data.txt', 'r')
file.write('Hello') # io.UnsupportedOperation: not writable
"""

"""
# This only opens for writing:
file = open('data.txt', 'w')
file.write('Hello')
file.seek(0)
data = file.read()  # io.UnsupportedOperation: not readable
"""
