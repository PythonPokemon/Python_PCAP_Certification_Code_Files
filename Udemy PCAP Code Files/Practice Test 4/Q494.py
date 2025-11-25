
class Top:
    pass


class Left(Top):
    pass


class Right(Top):
    pass


class Bottom1(Left, Right):
    pass


class Bottom2(Left, Top):
    pass


# class Bottom3(Top, Left):
#     pass
# TypeError: Cannot create a consistent method
# resolution order (MRO) for bases Top, Left

class Bottom4(Top, Right):
    pass
# TypeError: Cannot create a consistent method
# resolution order (MRO) for bases Top, Right
