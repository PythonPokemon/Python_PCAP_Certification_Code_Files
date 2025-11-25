
from functools import reduce
num = reduce(lambda x, y: x if (x > y) else y, [47, 11, 42, 102, 23])
print(num)  # 102
