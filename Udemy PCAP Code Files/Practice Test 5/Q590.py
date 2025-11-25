
class A1:
    def __init__(self):
        print(True)


class B2(A1):
    pass


b1 = B2()  # True
# As B doesn't define its own constructor,
# the constructor of its superclass is invoked
# and True is printed.


class A2:
    def __init__(self, value=True):
        print(value)


a2 = A2()  # True
# The value of the default parameter is used
# and True is printed.


class A4:
    # def __init__(self):
    def __init__():
        print(True)


# a4 = A4()
# TypeError: __init__() takes 0 positional arguments but 1 was given
# The constructor is missing its self parameter.


class A3:
    def __init__(self, value=True):
        print(value)


class B3(A3):
    def __init__(self, value=False):
        super().__init__(value)


b3 = B3()  # False
# The subclass defines its own constructor
# which passes the value False to its superclass
# where False is then printed.
