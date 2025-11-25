
# x = int(input())  # Input: 3
# y = int(input())  # Input: 2
x, y = 3, 2         # Just for convenience
x = x % y
print(3 % 2)  # 1
x = x % y
print(1 % 2)  # 1
print(x)
print(y)
y = y % x
print(2 % 1)  # 0
print(y)      # 0
