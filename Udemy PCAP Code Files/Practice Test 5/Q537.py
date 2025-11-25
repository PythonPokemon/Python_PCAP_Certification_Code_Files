
# First execute the following to create the needed file:
text = '''Peter
Paul
Mary
'''
with open('data.txt', 'w') as f:
    f.write(text)

for line in open('data.txt', 'r'):
    print(line)

"""
Peter

Paul

Mary
"""

print(type(open('data.txt', 'r')))  # <class '_io.TextIOWrapper'>
print(hasattr(open('data.txt', 'r'), '__iter__'))  # True
