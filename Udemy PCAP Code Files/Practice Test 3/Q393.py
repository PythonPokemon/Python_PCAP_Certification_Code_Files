
class Top:
    value = 3

    def say(self):
        return self.value


class Middle(Top):
    value = 2


class Bottom(Middle):
    def say(self):
        return -self.value


short = Bottom()
tall = Top()
average = Middle()


print(average.value == 2)           # True
# The value attribute is present inside of the Middle class
# and therefore it will be defined there.

print(short.value == 2)             # True
# Same here,
# the value attribute is present inside of the Middle class
# and therefore it will be defined there.

print(tall.say() == 2)              # False
print(tall.say())  # 3
# tall is an instance of the Top class
# and therefore value is 3.

print(isinstance(average, Bottom))  # False
# An object is not an instance of its home class subclass.
