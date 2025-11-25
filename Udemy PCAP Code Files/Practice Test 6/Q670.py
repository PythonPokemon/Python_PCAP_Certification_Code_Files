
# First you have to run this to create the file:
with open('test.txt', 'w') as f:
    f.write('Hello world')

file = open('test.txt')
print(file.readlines())  # ['Hello world']
file.close()

file = open('test.txt')
print(file.read())  # Hello world
file.close()

file = open('test.txt')
for f in file:
    print(f)  # Hello world
file.close()
