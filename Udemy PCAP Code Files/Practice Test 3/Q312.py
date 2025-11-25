
data = [
    lambda x: x ** 2,
    lambda x: x ** 3,
    lambda x: x ** 4
]

for func in data:
    print(func(3), end=' ')  # 9 27 81

"""
3 ** 2 -> 9
3 ** 3 -> 27
3 ** 4 -> 81
"""
