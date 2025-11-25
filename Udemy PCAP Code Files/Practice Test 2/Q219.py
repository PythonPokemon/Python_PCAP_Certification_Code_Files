
data = 'abcdefg'


def func(text):
    # del text[2]  # TypeError: ...
    return text


print(func(data))

# Strings are immutable
# The indexes are readable but not writeable:
s = 'Hello'
print(s[0])   # H
# s[0] = 'h'  # TypeError: ...
