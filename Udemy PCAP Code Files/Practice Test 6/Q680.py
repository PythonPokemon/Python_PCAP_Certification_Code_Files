
letters = 'zyx'

tmp = list(letters)
print(tmp)  # ['z', 'y', 'x']
tmp.sort()
print(tmp)  # ['x', 'y', 'z']
new_string = ''.join(tmp)
print(new_string)  # xyz
# The list() function turn the string into a list.
# The sort() method sorts the list in-place.
# The join() method turn the list into a string again.

new_string = ''.join(sorted(letters))
print(new_string)  # xyz
# The sorted() function retruns a sorted list.
# The join() method turn the list into a string again.

new_string = sorted(letters)
print(new_string)  # ['x', 'y', 'z']
# The result is sorted, but not a string.

# tmp = letters.sort()
# AttributeError: 'str' object has no attribute 'sort'
# new_string = str(tmp)
# Strings don't have a sort() method.
