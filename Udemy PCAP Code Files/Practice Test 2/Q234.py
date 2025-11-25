
# x = int(input())  # Input: 11
# y = int(input())  # Input: 4
x, y = 11, 4    # Just for convenience
x = x % y
print(11 % 4)  # 3
x = x % y
print(3 % 4)   # 3
y = y % x
print(4 % 3)   # 1
print(y)       # 1
