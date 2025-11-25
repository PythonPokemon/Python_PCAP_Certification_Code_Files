
# First you have to run this to create the file:
text = '''Lorem ipsum dolor sit amet,
consectetur adipisicing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
'''
with open('wellert.txt', 'w') as f:
    f.write(text)

try:
    file = open('wellert.txt', 'r')
    data = file.read()         # works
    # data = file.readline()   # reads only one line
    # data = file.readlines()  # reads every line, but as a list
    # data = file.load()       # Something went wrong!
    print(data)
except:
    print('Something went wrong!')
