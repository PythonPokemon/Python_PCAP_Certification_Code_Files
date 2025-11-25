
class Diamond:
    pass


class Adamant(Diamond):
    pass


class Gem(Diamond):
    pass


class Jewel1(Adamant, Diamond):
    pass


class Jewel2(Adamant, Gem):
    pass


# class Jewel3(Diamond, Adamant):
#     pass
# TypeError: Cannot create a consistent method
# resolution order (MRO) for bases Diamond, Adamant


# class Jewel(Diamond, Gem):
#     pass
# TypeError: Cannot create a consistent method
# resolution order (MRO) for bases Diamond, Gem
