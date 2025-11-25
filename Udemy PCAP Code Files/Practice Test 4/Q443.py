
# First execute the following to create the needed file:
text = '''Peter
Paul
Mary
'''
with open('data.txt', 'w') as f:
    f.write(text)


def get_data(filename, mode):
    import os
    if os.path.isfile(filename):
        with open(filename, mode) as file:
            return file.readline()
    else:
        return


print(get_data('data.txt', 'r'))     # Peter
print(get_data('anyfile.txt', 'r'))  # None
