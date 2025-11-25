
data = [1, 2, [3, 4], [5, 6], 7, [8, 9]]
count = 0

print(len(data))  # 6

for i in range(len(data)):  # 0 - 5
    if type(data[i]) == list:
        count += 1

print(count)  # 3

print(data[0])  # 1
print(type(data[0]))  # <class 'int'>
print(type(data[0]) == int)   # True
print(type(data[0]) == list)  # False

print(data[2])                # [3, 4]
print(type(data[2]))          # <class 'list'>
print(type(data[2]) == list)  # True

