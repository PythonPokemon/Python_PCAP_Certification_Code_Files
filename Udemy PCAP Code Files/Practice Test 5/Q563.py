
for i in dir(__builtins__):
    if i in ('hasattr', 'hasvar', 'hasprop'):
        print(i)  # hasattr


class Dog:
    def __init__(self, name):
        self.name = name


dog1 = Dog('Janosch')
print(hasattr(dog1, 'name'))  # True
