
def fun(n):
    s = '+'
    for i in range(n):
        s += s
        yield s


for x in fun(2):
    print(x)
"""
++
++++
"""


def fun(n):
    s = '+'
    for i in range(n):
        s += s
        return s


for x in fun(2):
    print(x)
"""
+
+
"""
