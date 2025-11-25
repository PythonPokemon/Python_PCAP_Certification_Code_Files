
# First execute the following to create the needed folder and file:
import os
if not os.path.isdir('a'):
    os.mkdir('a')

text = '''
def c():
    print("I am my_function, goo goo g'joob!")
'''
with open('a/b.py', 'w') as f:
    f.write(text)


import a.b
a.b.c()  # I am my_function, goo goo g'joob!

# c()  # NameError: name 'c' is not defined

#b.c()  # NameError: name 'b' is not defined
