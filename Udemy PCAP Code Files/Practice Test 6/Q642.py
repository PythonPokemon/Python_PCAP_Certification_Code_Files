
# First execute the following to create the needed file:
functions = '''
def func():
    print('Hello world')
'''
with open('functions.py', 'w') as f:
    f.write(functions)

index = '''
import functions
functions.func()
'''
with open('index.py', 'w') as f:
    f.write(index)
