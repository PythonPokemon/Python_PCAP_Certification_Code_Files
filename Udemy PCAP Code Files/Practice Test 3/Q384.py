
# First execute the following to create the needed file:
data = '''Peter
Paul
Mary
'''
with open('data.txt', 'w') as f:
    f.write(data)

file = open('data.txt', 'r')
print(file.readline())   # Peter

print(file.readlines())  # ['Paul\n', 'Mary\n']

# print(file.readstr())
# AttributeError: '_io.TextIOWrapper'
# object has no attribute 'readstr'

# print(file.readln())
# AttributeError: '_io.TextIOWrapper'
# object has no attribute 'readln'
