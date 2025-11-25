
data = open('data.txt', 'wb')
print(type(data))     # <class '_io.BufferedWriter'>
# print(data.read())  # io.UnsupportedOperation: read

data = open('data.txt', 'wb+')
print(type(data))     # <class '_io.BufferedRandom'>
print(data.read())    # b''

data = open('data.txt', 'w')
print(type(data))     # <class '_io.TextIOWrapper'>

data = open('data.txt', 'w+')
print(type(data))     # <class '_io.TextIOWrapper'>
