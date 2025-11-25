
# print('Whether 'tis nobler in the mind to suffer')
# SyntaxError: invalid syntax
# You cannot use a sinle quote inside of a string
# that is itself delimited by single quotes.

# print('''To be, or not to be,
# that is the question""")
# SyntaxError: EOF while scanning triple-quoted string literal
# If a multi-line string starts with three single quotes
# it has to end with three single quotes.

print("this is a quote: \"")  # this is a quote: "
# In a string that is delimited with double quotes
# you have to escape all double quotes.

print("\\")  # \
# You have to escape the backslash
# in order for it not to escape the double quotes.
