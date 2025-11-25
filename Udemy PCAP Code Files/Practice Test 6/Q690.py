
class Lower:
    def __init__(self):
        self.color = "blue"


print(Lower().color)  # blue


class Working:
    def __init__(self):
        raise KeyError


working = Working()  # KeyError


class Middle:
    def __init__():
        self.color = None


# middle = Middle()
# TypeError: __init__() takes 0 positional
# arguments but 1 was given


class Upper:
    def __init__(self):
        return False


# upper = Upper()
# TypeError: __init__() should return None, not 'bool'
