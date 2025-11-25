
class Test:
    def __init__(self, id):
        self.id = id
        id = 100  # This is a local variable of this method


x = Test(23)
print(x.id)  # 23
