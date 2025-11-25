
# First execute the following to create the needed file:
data = '''Peter
Paul
Mary
'''
with open('data.txt', 'w') as f:
    f.write(data)

file = open('data.txt', 'at')
file.write('Jane')
file.close()

with open('data.txt', 'r') as f:
    print(f.read())
"""
Peter
Paul
Mary
Jane
"""

print('----------')

# This would open for writing and reading
file = open('data.txt', 'at+')
file.seek(0)
print(file.read())
file.close()

"""
Peter
Paul
Mary
Jane
"""

file = open('data.txt', 'ab')
# file.write('Jane')  # TypeError: ...
file.close()

file = open('data.txt', 'ab+')
# file.write('Jane')  # TypeError: ...
file.close()
