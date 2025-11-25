
# First you have to run this to create the file:
with open('my_module.py', 'w') as f:
    f.write("print('I am inside the file: ', __name__)")

import my_module  # I am inside the file:  my_module
