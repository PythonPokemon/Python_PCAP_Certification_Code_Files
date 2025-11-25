
class Aleph:
    def __init__(self):
        self.attribute = True


print(Aleph().attribute)  # True


class Bet:
    def __init__(self):
        raise ArithmeticError


# bet = Bet()  # ArithmeticError


class Dalet:
    def __init__(self):
        # return None
        return False


# dalet = Dalet()
# TypeError: __init__() should return None, not 'bool'


class Gimel:
    # def __init__(self):
    def __init__():
        self.attribute = True


gimel = Gimel()
# TypeError: __init__() takes 0 positional arguments but 1 was given
