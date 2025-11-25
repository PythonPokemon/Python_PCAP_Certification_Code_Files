
# First execute the following to create the needed files:
text = '''
print('x', end='')
'''
with open('x.py', 'w') as f:
    f.write(text)

text = '''
import x
print('y', end='')
'''
with open('y.py', 'w') as f:
    f.write(text)

text = '''
print('z', end='')
import x
import y
'''
with open('z.py', 'w') as f:
    f.write(text)

import z  # zxy
