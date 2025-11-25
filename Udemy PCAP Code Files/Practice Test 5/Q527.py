
class B:
    def __init__(self):
        print("I am a method, goo goo g'joob!")


class A(B):
    def __init__(self):
        super().__init__()
        B.__init__(self)
        # B.__init__()            # TypeError: ...
        # super().__init__(self)  # TypeError: ...


A()
