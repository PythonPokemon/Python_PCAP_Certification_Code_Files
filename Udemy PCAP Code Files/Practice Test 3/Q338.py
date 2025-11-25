
# When you open a file for reading,
# if the file does not exist, an error occurs:
# open('anyfile.txt', 'r')  # FileNotFoundError: ...

# When you open a file for writing,
# if the file does not exist, a new file is created:
file = open('peoples.txt', 'w')
file.write('Peter, Paul, Mary')
file.close()
file = open('peoples.txt', 'r')
print(file.read())  # Peter, Paul, Mary
file.close()

# When you open a file for writing, if the file exists,
# the existing file is overwritten with the new file:
file = open('peoples.txt', 'w')
file.close()
file = open('peoples.txt', 'r')
print(file.read())  # no output, because the file is empty
file.close()
