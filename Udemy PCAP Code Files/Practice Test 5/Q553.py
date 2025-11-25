
# First execute the following to create the needed file:
with open('index.txt', 'w') as f:
    f.write('Peter, Paul, Mary')

x = open('index.txt', 'r')
print(x.read(1))  # P
