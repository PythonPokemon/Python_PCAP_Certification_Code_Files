
class Class:
    class_var = 1

    def __init__(self):
        self.instance_var = 1

    def method(self):
        pass


object = Class()

print(Class.__dict__['method'] != None)      # True
print(Class.__dict__['method'] is not None)  # True
print(Class.__dict__)
# {... 'method': <function Class.method at <hex number>>, ...}
print(Class.__dict__['method'])
# <function Class.method at <hex number>>
# Object methods are included in the class's __dict__.

print('__dict__' in Class.__dict__)          # True
print(Class.__dict__['__dict__'])
# <attribute '__dict__' of 'Class' objects>
# As any other variable __dict__ is included in __dict__.

print(len(object.__dict__) == len(Class.__dict__))  # False
print(len(object.__dict__))  # 1
print(len(Class.__dict__))   # 7
print(object.__dict__)       # {'instance_var': 1}
# The object' __dict__ only includes instance_var.

# print(object.__dict__['method'] != None)  # KeyError: 'method'
# Methods are not included in an object's __dict__.
