
def I():
    s = 'abcdef'
    for c in s[::2]:
        yield c


for x in I():
    print(x)
"""
a
c
e
"""


def I():
    s = 'abcdef'
    for c in s[::2]:
        return c


for x in I():
    print(x)  # a
