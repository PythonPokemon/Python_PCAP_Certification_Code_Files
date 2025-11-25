
class Test:
    def __init__(self, x=0):
        self.x = x


# obj = Test(1, 2)  # TypeError: ...
obj = Test(1)
obj = Test()
obj = Test(None)
