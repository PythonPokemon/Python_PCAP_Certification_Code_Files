
file = open('data.txt', 'r')
# file = open('data.txt', 'r+')
txt = "I'm gonna make him an offer he can't refuse."
file.writelines(txt)  # io.UnsupportedOperation: not writable
file.seek(0)
lines = file.readlines()
print(lines)
file.close()
