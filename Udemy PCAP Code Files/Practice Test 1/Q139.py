
# First execute the following to create the needed file:
text = '''
print("I am a module, goo goo g'joob!")
'''
with open('module.py', 'w') as f:
    f.write(text)

import module  # I am a module, goo goo g'joob!
import module
