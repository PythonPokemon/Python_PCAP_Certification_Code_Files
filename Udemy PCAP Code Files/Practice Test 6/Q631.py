
# data = eval(input('Input: '))
data = eval('[x**2 for x in range(1, 4)]')
print('Input: [x**2 for x in range(1, 4)]')
print('Output:', data)  # Output: [1, 4, 9]
print('----------')

# If there is a string in the input,
# it would need quotation marks:

# data = eval(input('Input: '))
# data = eval('Hello Python')  # SyntaxError: ...

# data = eval(input('Input: '))
data = eval('"Hello Python"')
print('Input: "Hello Python"')
print('Output:', data)  # Hello Python
