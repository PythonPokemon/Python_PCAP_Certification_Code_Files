
try:
    file = open('data.txt', 'r')
    file.write('Hello file!')
except:
    print('An error occurred.')  # An error occurred.
else:
    print('The content is written successfully.')

# This happens, when the file doesn't exist:
# file = open('data.txt', 'r')   # FileNotFoundError

# This happens, when the file exists:
file = open('data.txt', 'w')
file.close()
file = open('data.txt', 'r')
# file.write('Hello file!'). # io.UnsupportedOperation: not writable
