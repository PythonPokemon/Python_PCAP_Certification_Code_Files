
def fun(x):
    return 1 / x


def mid_level(x):
    try:
        fun(x)
    except:
        raise AssertionError
    else:
        return 0


try:
    x = mid_level(0)
except Exception:
    x = -1
except:
    x = -2

print(x)  # -1
