
# First execute the following to create the needed folder and file:
import os
if not os.path.isdir('p'):
    os.mkdir('p')
text = '''
def f():
    print("I am my_function, goo goo g'joob!")
'''
with open('p/m.py', 'w') as f:
    f.write(text)

from p.m import f
f()  # I am my_function, goo goo g'joob!

import p.m
p.m.f()  # I am my_function, goo goo g'joob!

import p
# m.f()  # NameError: name 'm' is not defined

# import p.m.f
# ModuleNotFoundError: No module named 'p.m.f'; 'p.m' is not a package
