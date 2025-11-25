
class Constructor:
    def __init__(self):
        self.value = "Hello"


constructor = Constructor()
print(constructor.value)  # Hello
# In Python, the constructor is a function called __init__().
# You can use it to initialize the new object's state.


class Encapsulation:
    def __init__(self):
        self.__value = "World"


encapsulation = Encapsulation()
# print(encapsulation.__value)
# AttributeError: ...
# Encapsulation lets you hide sensitive object components
# and protect them from unauthorized modification.


class A:
    pass


a = A()
a.new = 7
print(a.new)  # 7

b = A()
b.anoter_new = 11
print(b.anoter_new)  # 11
# In Python each object of the same class
# can have different attributes.
