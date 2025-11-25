
class Collection:
    stamps = 2

    def __init__(self, stuff):
        self.stuff = stuff

    def dispose(self):
        del self.stuff

binder = Collection(1)
print(binder.__dict__)           # {'stuff': 1}
binder.dispose()

print('stamps' in Collection.__dict__)                   # True
print(Collection.__dict__)  # {... 'stamps': 2, ...}
# stamps is a class variable
# and is included in the class's __dict__.

print(len(binder.__dict__) != len(Collection.__dict__))  # True
print(binder.__dict__)           # {}
print(len(binder.__dict__))      # 0
print(len(Collection.__dict__))  # 7
print(Collection.__dict__)
"""{
'__module__': '__main__',
'stamps': 2,
'__init__': <function Collection.__init__ at 0x100c28f40>,
'dispose': <function Collection.dispose at 0x100c28fe0>,
'__dict__': <attribute '__dict__' of 'Collection' objects>,
'__weakref__': <attribute '__weakref__' of 'Collection' objects>,
'__doc__': None}
"""
# __dict__ of a class contains its attributes and methods
# and a few standard class attributes like __module__, __doc__, ...

print('stuff' in binder.__dict__)                        # False
# dispose() removed the stuff variable from the object's __dict__.

print(len(binder.__dict__) > 0)                          # False
print(len(binder.__dict__))  # 0
# The object's __dict__ is empty.
