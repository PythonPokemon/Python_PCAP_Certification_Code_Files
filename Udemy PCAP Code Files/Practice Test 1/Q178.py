
print(''.join(sorted("321")))  # 123
# The sorted() function retruns a sorted list.
# The join() method turns the list into a string again.

tmp = list("321")
tmp.sort()
print(''.join(tmp))  # 123
# The list() function turns the string into a list.
# The sort() method sorts the list in-place.
# The join() method turns the list into a string again.

print(sorted("321"))  # ['1', '2', '3']
# The result is sorted, but not a string.


# tmp = "321".sort()
# AttributeError: 'str' object has no attribute 'sort'
# print(str(tmp))
# Strings don't have a sort() method.
