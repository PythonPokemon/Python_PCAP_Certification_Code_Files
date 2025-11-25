
file = open('will_be_created.txt', 'w')
file.close()

# open('does_not_exist.txt', 'r')  # FileNotFoundError: ...

file = open('will_be_created.txt', 'r')
# file.write("Hello")
# io.UnsupportedOperation: not writable


# Cleanup code (to remove the file again):
# import os
# os.remove("will_be_created.txt")
