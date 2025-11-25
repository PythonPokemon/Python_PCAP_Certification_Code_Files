
x = True
y = False
z = False

if x or y and z:
    print('TRUE')                 # TRUE
else:
    print('FALSE')

print(x or y and z)               # True
print(True or False and False)    # True
print(True or (False and False))  # True
print(True or False)              # True
print(True)                       # True
