
s = '2A'

try:
    n = int(s)
except TypeError:
    n = 3
except LookupError:
    n = 2
except:
    n = 1

print(n)  # 1
