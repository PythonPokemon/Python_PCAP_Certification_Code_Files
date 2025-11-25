
class Class:
    var = 1
    def __init__(self, value):
        self.prop = value

Object = Class(2)

print('var' in Class.__dict__)    # True

print(len(Object.__dict__) == 1)  # True

print('var' in Object.__dict__)   # False

print('prop' in Class.__dict__)   # False

