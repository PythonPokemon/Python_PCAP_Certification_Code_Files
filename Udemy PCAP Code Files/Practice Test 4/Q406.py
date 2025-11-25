
data1 = 'a', 'b'
data2 = ('a', 'b')
print(data1 == data2)  # True
print(data1 is data2)  # True
print(id(data1))       # e.g. 140539383900864
print(id(data2))       # e.g. 140539383900864 (the same number)
