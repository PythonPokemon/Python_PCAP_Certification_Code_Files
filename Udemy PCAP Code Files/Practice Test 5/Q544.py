
# First execute the following to create the needed folder and file:
with open('data.txt', 'w') as f:
    f.write('Hello')
import os
if not os.path.isdir('folder'):
    os.mkdir('folder')

# import os
print(os.path.isfile('data.txt'))  # True
print(os.path.isfile('folder'))    # False
print(os.path.exists('data.txt'))  # True
print(os.path.exists('folder'))    # True

# print(os.isfile('data.txt'))       # AttributeError: ...
# print(os.path.isFile('data.txt'))  # AttributeError: ...
