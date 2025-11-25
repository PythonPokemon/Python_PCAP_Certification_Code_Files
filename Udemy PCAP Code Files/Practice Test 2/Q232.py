
colors = ['red\n', 'yellow\n', 'blue\n']
file = open('wellert.txt', 'w+')
file.writelines(colors)
file.close()
file.seek(0)  # ValueError: I/O operation on closed file.
for line in file:
    print(line)
file.close()
