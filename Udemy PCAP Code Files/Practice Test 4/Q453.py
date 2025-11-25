
# First execute the following to create the needed file:
text = '''Peter
Paul
Mary
'''
with open('index.txt', 'w') as f:
    f.write(text)

f = open('index.txt', 'r')
data = f.readlines()
print(data)        # ['Peter\n', 'Paul\n', 'Mary\n']
print(type(data))  # <class 'list'>
f.close()
