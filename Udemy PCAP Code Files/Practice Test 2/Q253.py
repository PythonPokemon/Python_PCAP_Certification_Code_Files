
def func(data):
    for d in data[::2]:
        yield d


for x in func('abcdef'):
    print(x, end='')  # ace
print()


# Differnt example of a generater function:
def yield_test():
    yield "Mary"
    yield "had"
    yield "a"
    yield "little"
    yield "lamb."


for i in yield_test():
    print(i, end=" ")  # Mary had a little lamb.
