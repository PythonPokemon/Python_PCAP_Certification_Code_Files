
class BluePrint:
    __element = 1

    def __init__(self):
        self.component = 1

    def __action(self):
        pass


product = BluePrint()

product._BluePrint__action()

# product.__action()
# AttributeError: 'BluePrint'
# object has no attribute '__action'

# product._product__action()
# AttributeError: 'BluePrint'
# object has no attribute '_product__action'

# BluePrint._BluePrint__action()
# TypeError: __action() missing 1 required
# positional argument: 'self'
