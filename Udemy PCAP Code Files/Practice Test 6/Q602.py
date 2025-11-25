
data1 = (1, 2)
data2 = (3, 4)
[print(sum(x)) for x in [data1 + data2]]  # 10
[print(sum(x)) for x in [(1, 2, 3, 4)]]   # 10

[print(sum(x)) for x in [(1, 2), (3, 4), (5, 6)]]  # 3 - 7 - 11
