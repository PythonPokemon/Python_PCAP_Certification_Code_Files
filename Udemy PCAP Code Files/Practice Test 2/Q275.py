
# __name__
# First execute the following to create the needed file:
with open('my_module.py', 'w') as f:
    f.write('print(__name__)')

import my_module  # my_module


# __init__.py
# First execute the following to create the needed folder and file:
import os
if not os.path.isdir('my_package'):
    os.mkdir('my_package')

with open('my_package/__init__.py', 'w') as f:
    f.write("I am initialized!")

import my_package  # I am initialized!
