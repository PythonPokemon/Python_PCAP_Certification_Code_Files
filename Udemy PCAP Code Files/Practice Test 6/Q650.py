
# First execute the following to create the needed file:
data = '''Peter
Paul
Mary
'''
with open('data.txt', 'w') as f:
    f.write(data)

file = open('data.txt', 'r')
print(file.readline())        # Peter
print(file.readline())        # Paul
print(file.readline())        # Mary
print(type(file.readline()))  # <class 'str'>
print(bool(file.readline()))  # False
