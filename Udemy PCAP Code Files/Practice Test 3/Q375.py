
# First execute the following to create the needed file:
with open('my_module.py', 'w') as f:
    f.write('print(__name__)')

import my_module  # my_module

print(__name__)   # __main__
