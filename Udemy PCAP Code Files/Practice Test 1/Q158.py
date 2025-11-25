
def main(a, b, c, d):
    value = a + b * c - d         # 3
    # value = (a + (b * c)) - d   # 3
    # value = (a + b) * (c - d)   # -3
    # value = a + ((b * c) - d)   # 3
    return value


print(main(1, 2, 3, 4))  # 3
