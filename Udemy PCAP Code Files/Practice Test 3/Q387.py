
def attic(x):
    assert x != 0
    return 1 / x


def floor(x):
    try:
        attic(x)
    except:
        raise


try:
    x = attic(0)
except RuntimeError:
    x = -3
except:
    x = -2
else:
    x = -1
print(x)  # -2

# assert 0 != 0  # AssertionError
