
w = [7, 3, 23, 42]
x = w[1:]  # [3, 23, 42]
y = w[1:]  # [3, 23, 42]
z = w      # A reference
print(z)   # [7, 3, 23, 42]
y[0] = 10  # Changes only y
z[1] = 20  # Changes z and w
print(w)   # [7, 20, 23, 42]

print(id(x))  # e.g. 140539383900864
print(id(y))  # e.g. 140539383947456 (a different number)
print(id(w))  # e.g. 140539652049216 (the same number than z)
print(id(z))  # e.g. 140539652049216 (the same number than w)
