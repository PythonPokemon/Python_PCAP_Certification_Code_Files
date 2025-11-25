
class Storage:
    def __init__(self):
        self.rack = 1

    def get(self):
        return self.rack

    def print(self):
        print(Storage.get(self))
        print(self.get())


stuff = Storage()
stuff.print()
# 1
# 1
