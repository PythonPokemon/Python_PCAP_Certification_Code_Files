
# First execute the following to create the needed file:
with open('index.txt', 'w') as f:
    f.write('Peter\n')
    f.write('Paul\n')
    f.write('Mary\n')

file = open('index.txt', 'r')
print(file.readlines(10))
# Peter
# Paul
