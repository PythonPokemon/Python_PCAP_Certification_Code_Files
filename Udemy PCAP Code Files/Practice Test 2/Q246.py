
def func(a=1, b=1, c=2):
    pass


# def func(a=1, b): pass            # SyntaxError: ...
# def func(a=1, b, c=2): pass       # SyntaxError: ...
# def func(a=1, b=1, c=2, d): pass  # SyntaxError: ...

# This would also work:
def func(a, b=1, c=2):
    pass


"""
def func(a=1, b): pass
func(7)
The 7 would go into a and there is nothing left for b.
"""