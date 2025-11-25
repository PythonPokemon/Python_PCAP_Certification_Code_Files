
s = "12"
s = s[1::2]
print(s)    # 2
# The element at index 1 will be the only element.

s = "12"
s = s[-1]
print(s)    # 2
# -1 is the last element

s = "12"
s = s[-3:-5]
print(s)    # NO OUTPUT
# There is no third last or fifth last element.

s = "rhyme"
# s = s[9]  # IndexError: string index out of range
# There is no element with the index 9.
