
# First execute the following to create the needed file:
data = '''Peter
Paul
Mary
'''
with open('data.txt', 'w') as f:
    f.write(data)

file = open('data.txt', 'r')
print(file.readline())  # Peter
print(file.readline())  # Paul
print(file.readline())  # Mary

print('----------')

file = open('data.txt', 'r')
print(file.readline())   # Peter
print(file.readlines())  # ['Paul\n', 'Mary\n']

print('----------')

file = open('data.txt', 'r')
print(file.readline())  # Peter
print(file.read())      # Paul Mary

print('----------')

n = 7
file = open('data.txt', 'r')
print(file.readline())  # Peter
print(file.read(n))     # Paul Ma
