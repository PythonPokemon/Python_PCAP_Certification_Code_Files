
# First you have to run this to create the file:
with open('alphabet.bin', 'wb') as f:
    f.write(bytes([65, 66, 67]))

with open('alphabet.bin', 'rb') as f:
    b1 = f.read()
print(b1)        # b'ABC'
print(type(b1))  # <class 'bytes'>
