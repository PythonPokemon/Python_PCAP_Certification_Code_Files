
def func(data):
    data = [7, 23, 42]
    print('Function scope: ', data)  # [7, 23, 42]


data = ['Peter', 'Paul', 'Mary']
func(data)
print('Outer scope: ', data)  # ['Peter', 'Paul', 'Mary']
