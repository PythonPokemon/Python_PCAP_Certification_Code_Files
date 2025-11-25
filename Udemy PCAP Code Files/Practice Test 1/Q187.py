
data = [261, 321]
try:
    print(data[-3])
except Exception as exception:
    print(exception.args)  # ('list index out of range',)
else:
    print("('success',)")

# print([261, 321][-3])
# IndexError: list index out of range
