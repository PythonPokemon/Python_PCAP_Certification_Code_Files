
def remove_min(s):
    assert type(s) == list
    assert len(s) > 0
    m = min(s)
    s.remove(m)
    return s


print(remove_min([1, 2, 3]))  # [2, 3]
# print(remove_min('Hello'))  # ... AssertionError
# print(remove_min([]))       # ... AssertionError
