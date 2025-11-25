
# First execute the following to create the needed folder and file:
text = '''
def func():
    print("I am my_function, goo goo g'joob!")
'''
with open('modu.py', 'w') as f:
    f.write(text)


import modu
modu.func()


import sys
print(sys.path)
# ['/Users/cordm/.../Practice Test 5',
# '/Users/cordm/...',
# '/Library/Frameworks/Python.framework/Versions/3.9/lib/python39.zip',
# '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9',
# '/Library/Frameworks/.../Versions/3.9/lib/python3.9/lib-dynload',
# '/Users/cordm/Library/Python/3.9/lib/python/site-packages',
# '/Library/Frameworks/.../Versions/3.9/lib/python3.9/site-packages']
