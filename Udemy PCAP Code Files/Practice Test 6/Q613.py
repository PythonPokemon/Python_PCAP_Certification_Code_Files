
res = str(bool(1) + float(12) / float(2))
print(res)                                  # 7.0
print(str(bool(1) + float(12) / float(2)))  # 7.0
print(str(True + 12.0 / 2.0))               # 7.0
print(str(True + (12.0 / 2.0)))             # 7.0
print(str(True + 6.0))                      # 7.0
print(str(1 + 6.0))                         # 7.0
print(str(7.0))                             # 7.0
print('7.0')                                # 7.0
