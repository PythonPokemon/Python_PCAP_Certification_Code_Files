
import errno

try:
    fp = open("no_such.file")
except IOError as error:
    if error.args[0] == errno.ENOENT:
        print("No such file or directory")

# ENOENT
# Error NO ENTry
# Error NO ENTity
