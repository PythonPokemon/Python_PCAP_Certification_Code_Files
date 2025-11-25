
b = bytearray(3)
print(b)  # bytearray(b'\x00\x00\x00')

# The bytearray works better with sequences of integers:
print(bytearray([3]))  # bytearray(b'\x03')
print(bytearray([65, 66, 67]))  # bytearray(b'ABC')
