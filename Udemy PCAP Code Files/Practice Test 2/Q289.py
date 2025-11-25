
import math

x = -1.7
print(-abs(math.floor(x) + math.ceil(x)))        # -3
print(-abs(math.floor(-1.7) + math.ceil(-1.7)))  # -3
print(math.floor(-1.7))  # -2
print(math.ceil(-1.7))   # -1
print(-abs(-2 + -1))                             # -3
print(-2 + -1)                                   # -3
print(-abs(-3))                                  # -3
print(abs(-3))  # 3
print(-3)                                        # -3
