
# First execute the following to create the needed folder and file:
import os
if not os.path.isdir('my_package'):
    os.mkdir('my_package')
text = '''
def my_function():
    print("I am my_function, goo goo g'joob!")
'''
with open('my_package/my_module.py', 'w') as f:
    f.write(text)

from my_package.my_module import my_function
my_function()  # I am my_function, goo goo g'joob!
