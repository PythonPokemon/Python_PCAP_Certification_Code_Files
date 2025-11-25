
# "Multiplication precedes addition." is true:
print(3 + 4 * 5)    # 23
print(3 + (4 * 5))  # 23
print(3 + 20)       # 23
print(23)           # 23

# "The ** operator uses right sided binding." is true:
print(2 ** 3 ** 2)    # 512
print(2 ** (3 ** 2))  # 512
print(2 ** 9)         # 512
print(512)            # 512

# "The right argument of the % operator cannot be zero."
# is true:
# print(7 % 0)  # ZeroDivisionError: ...

# "The result of the / operator is always an integer value."
# is false:
print(9 / 3)  # 3.0
# The result of the division operator is always a float value!
