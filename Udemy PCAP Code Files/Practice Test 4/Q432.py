
print(list('a'.encode()))          # [97]
print(list('a'.encode('utf-8')))   # [97]
print(list('a'.encode('utf-16')))  # [255, 254, 97, 0]
print(list('a'.encode('utf-32')))  # [255, 254, 0, 0, 97, 0, 0, 0]
