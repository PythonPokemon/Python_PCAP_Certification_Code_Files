
header = 2 * '+-' + '+'
print(header)  # +-+-+
plus = 0
for x in header:
    print(x)
    if x not in header:
        plus += 1
print(plus)  # 0
