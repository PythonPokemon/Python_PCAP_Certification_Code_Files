
data = [1, 5, 10, 19, 55, 30, 55, 99]
data.pop(5)
data.remove(19)
data.remove(55)
data.remove(55)
print(data)     # [1, 5, 10, 99]

data = [1, 5, 10, 19, 55, 30, 55, 99]
data.remove(5)
data.remove(19)
data.remove(55)
print(data)     # [1, 10, 30, 55, 99]

data = [1, 5, 10, 19, 55, 30, 55, 99]
data.pop(5)
# data.pop(19)  # IndexError: pop index out of range
# data.pop(55)  # IndexError: pop index out of range

data = [1, 5, 10, 19, 55, 30, 55, 99]
data.pop(1)
data.pop(3)
data.pop(4)
# data.pop(6)   # IndexError: pop index out of range
