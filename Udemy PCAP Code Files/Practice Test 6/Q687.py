
# First execute the following to create the needed file:
data = '''Peter
Paul
Mary
'''
with open('existing_text_file', 'w') as f:
    f.write(data)


try:
    f = open("existing_text_file", "rt")
    spam = f.readlines()
    print(len(spam))       # 3
    f.close()
except IOError:
    print(-1)
