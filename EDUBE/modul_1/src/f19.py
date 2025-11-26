"""
Selected functions from the platform module: continued
The python_implementation and the python_version_tuple functions

If you need to know what version of Python is running your code, 
you can check it using a number of dedicated functions - here are two of them:

-python_implementation() → returns a string denoting 
    the Python implementation (expect CPython here, unless you decide to use 
    any non-canonical Python branch)

-python_version_tuple() → returns a three-element tuple filled with:
    the 'major' part of Python's version;
    the 'minor' part;
    the 'patch' level number.
"""

from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)
