
file = open('data.txt', 'w+')
print('Name of the file: ', file.name)  # Name of the file: data.txt

s = 'Peter Wellert\nHello everybody'
file.write(s)
"""
# The contents of the file will look like that:
Peter Wellert
Hello everybody
# (with an unvisible newline character at the end of the first line)
"""

# The file position gets set back to the beginning of the file:
file.seek(0)

# The for loop iterates through the file line by line:
for line in file:
    print(line)
"""
# Output of the for loop:
Peter Wellert

Hello everybody
"""

file.close()
