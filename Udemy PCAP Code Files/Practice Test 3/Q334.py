
class A:
    def __init__(self, x=0):
        self.x = x


obj1 = A(23)
obj2 = A(23)
print(id(obj1) == id(obj2))  # False
print(id(obj1))  # e.g. 140539383900864
print(id(obj2))  # e.g. 140539652049216 (a different number)

str1 = 'Hello'
str2 = 'Hello'
print(id(str1) == id(str2))  # True
print(id(str1))  # e.g. 140539383947452
print(id(str2))  # e.g. 140539383947452 (the same number)
