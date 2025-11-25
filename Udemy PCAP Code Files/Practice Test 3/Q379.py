
print('' in '')               # True
# An empty string is treated as if
# it was an (invisible) part of every string.
# Even of the empty string.

print('de' not in 'abc')      # True
# Yes, 'de' is not in 'abc'.

print('?' in '')              # False
# '?' is not part of the empty string.

print(not 'xyz' in 'uvwxyz')  # False
print('xyz' not in 'uvwxyz')  # False
# No, 'xyz' is in 'uvwxyz'
