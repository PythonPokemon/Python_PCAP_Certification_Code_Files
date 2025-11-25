
print('bc' in 'abc')          # True
# Yes, "bc" is a part of "abc"

print('' in 'alphabet')       # True
# An empty string is treated as if
# it was an (invisible) part of every string.

print('' not in '')           # False
# An empty string is treated as if
# it was an (invisible) part of every string.
# Even of the empty string.

print('xyz' not in 'uvwxyz')  # False
# "xyz" is a part of "uvwxyz".
