
x = 0
while x < 6:
    print('1. x:', x)         # 0 -> 1 -> 2 -> 3 -> 4 -> 5
    x += 1
    print('2. x:', x)         # 1 -> 2 -> 3 -> 4 -> 5 -> 6
    if x % 2 == 0:
        print('x in if:', x)  # 2 -> 4 -> 6
        continue
    print('x behind if:', x)  # 1 -> 3 -> 5
    print('*')
"""
*
*
*
"""
