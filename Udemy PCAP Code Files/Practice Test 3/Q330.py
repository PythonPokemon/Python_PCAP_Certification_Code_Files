
print('is' in 'This IS Python code.')  # True

print('t' in 'Peter')                  # True

x = 42
y = 42
print(x is not y)                      # False

x = 'Peter Wellert'
y = 'Peter Wellert'.lower()
print(x is y)                          # False
x = 'Peter Wellert'
y = 'Peter Wellert'
print(x is y)                          # True

x = ['Peter', 'Paul', 'Mary']
y = ['Peter', 'Paul', 'Mary']
print(x is y)                          # False
print(x == y)                          # True
