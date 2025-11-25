
class MyClass:
    def __init__(self, initial):
        self.store = initial

    def put(self, new):
        self.store.append(new)

    def get(self):
        return self.store

    def dup(self):
        # insert the line of code here
        self.put(self.get()[-1])  # [0, 1, 1]
        # self.put(self.store[1])   # [0, 1, 1]
        # self.put.store(1)         # AttributeError
        # put(self.store(1))        # NameError

Object = MyClass([0])
Object.put(1)
Object.dup()
print(Object.get())

