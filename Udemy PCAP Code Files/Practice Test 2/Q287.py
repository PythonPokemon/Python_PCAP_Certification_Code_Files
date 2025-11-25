
try:
    f = open("non_existing_file", "w")
    print(1, end=" ")  # 1
    s = f.readline()
    print(2, end=" ")
except IOError as error:
    print(3, end=" ")  # 3
else:
    f.close()
    print(4, end=" ")

f = open("non_existing_file", "w")
# s = f.readline()
# io.UnsupportedOperation: not readable


# Cleanup code (to remove the file again):
# import os
# os.remove("non_existing_file")
