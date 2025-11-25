
class Class:
    def __init__(self):
        self.x = 23


object = Class()
print(object.x)  # 23

object = Class  # Creates a reference
# print(object.x)  # AttributeError ...

a = object()
print(a.x)  # 23

# object = Class(self)  # NameError ...

# object = Class(object)  # TypeError ...
