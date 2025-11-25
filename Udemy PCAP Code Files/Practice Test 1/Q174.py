
# First execute the following to create a file with already existing lines
with open('file', 'w') as f:
    for i in range(1, 6):
        f.write(str(i) + '. Line\n')


for x in open('file', 'rt'):
    print(x)
