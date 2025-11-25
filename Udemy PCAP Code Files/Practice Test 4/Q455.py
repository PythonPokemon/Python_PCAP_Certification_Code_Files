
# First you have to run this to create the file:
with open('peoples.txt', 'w') as f:
    f.write('Peter:10\nPaul:20\nMary:30\nJane:40')

points = 0
try:
    file = open('peoples.txt', 'r')
    data = file.readlines()
    # Reads all lines and puts them in a list
    print('content:', data)
    # ['Peter:10\n', 'Paul:20\n', 'Mary:30\n', 'Jane:40']
    for d in data:
        print('d:', d)
        # Peter:10 -> Paul:20 -> Mary:30 -> Jane:40
        print("d.split(':')[1]:", d.split(':')[1])
        # 10 -> 20 -> 30 -> 40
        points += float(d.split(':')[1])
        # 10.0 + 20.0 + 30.0 + 40.0 -> 100.0
    file.close()
except:
    print('The file could not be opened!')

print(points)
