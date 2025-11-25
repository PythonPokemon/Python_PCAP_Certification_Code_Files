
# """
f = open('data.txt', 'w')
f.write('Hello world')
f.close()
# """

"""
f = open('data.txt')
f.write('Hello world')  # io.UnsupportedOperation: ...
f.close()
"""

"""
f = open('data.txt', 'r')
f.write('Hello world')  # io.UnsupportedOperation: ...
f.close()
"""

"""
f = open('data.txt', 'b')
f.write('Hello world')  # ValueError: ...
f.close()
"""
