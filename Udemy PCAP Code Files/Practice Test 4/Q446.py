
# First execute the following to create the needed file:
text = '''
def func():
    print("I am a function, goo goo g'joob!")
'''
with open('mod.py', 'w') as f:
    f.write(text)

from mod import func
func()  # I am a function, goo goo g'joob!
