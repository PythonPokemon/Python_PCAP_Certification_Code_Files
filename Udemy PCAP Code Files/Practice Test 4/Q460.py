
from os import path
print(path.isfile('unknown.txt'))  # False

from os.path import isfile
print(isfile('unknown.txt'))  # False
