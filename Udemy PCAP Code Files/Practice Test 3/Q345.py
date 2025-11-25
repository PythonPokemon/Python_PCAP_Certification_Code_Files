
# First execute the following to create the needed file:
text = '''Peter
Paul
Mary
'''
with open('data.txt', 'w') as f:
    f.write(text)

import os                           # Line 01
def read_file(file):                # Line 02
    line = None                     # Line 03
    if os.path.isfile(file):        # Line 04
        data = open(file, 'r')      # Line 05
        while line != '':           # Line 06
            line = data.readline()  # Line 07
            print(line)             # Line 08

read_file('data.txt')
