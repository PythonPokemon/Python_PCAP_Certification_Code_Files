
class Storage:
    def __init__(self):
        self.rack = 1

    def get(self):
        return self.rack

stuff = Storage()
print(stuff.get())  # 1
