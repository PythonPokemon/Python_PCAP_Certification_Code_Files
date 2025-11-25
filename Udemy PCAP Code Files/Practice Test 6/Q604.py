
list = ['Peter', 'Paul', 'Mary']


# def func(data):
def list(data):
    del data[1]
    data[1] = 'Jane'
    return data


# print(func(list))  # ['Peter', 'Jane']
print(list(list))    # TypeError: ...
