
class Test:
    def __init__(self, s):
        self.s = s
        # s = s              # AttributeError: ...

    def print(self):
        print(s)             # NameError: ...
        # print(self.s)      # Hello Python


x = Test('Hello Python')
x.print()
