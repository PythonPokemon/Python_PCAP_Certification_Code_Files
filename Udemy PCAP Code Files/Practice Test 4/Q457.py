
class A:
    def __init__(self):
        self.text = 'abc'
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == len(self.text):
            raise StopIteration
        value = self.text[self.count]
        self.count += 1
        return value


for x in A():
    print(x, end='')  # abc
