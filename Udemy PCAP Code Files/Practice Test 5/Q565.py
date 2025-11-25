
# First you have to run this to create the files:
with open('alphabet.bin', 'wb') as f:
    f.write(bytes([65, 66, 67]))
with open('alphabet.txt', 'wt') as f:
    f.write('ABC')

with open('alphabet.bin', 'rb') as f:
    print(f.read())  # b'ABC'

with open('alphabet.txt', 'rt') as f:
    print(f.read())  # ABC
