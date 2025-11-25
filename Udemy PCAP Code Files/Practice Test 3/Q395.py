
class Un:
    value = "Eins"

    def say(self):
        return self.value.lower()


class Deux(Un):
    value = "Zwei"


class Troi(Un):
    def say(self):
        return self.value.upper()


class Quatre(Troi, Deux):
    pass


d = Quatre()
b = Deux()


print(Troi in Quatre.__bases__)  # True
# __bases__ holds the direct superclasses of a class
# and Troi is a direct superclass of Quatre.

print(isinstance(d, Un))         # True
# d is an instance of Quatre
# and therefore also an instance of the superclass Un.

print(b.say() == "ZWEI")         # False
print(b.say())  # zwei
# b is an instance of Deux
# and inherits the say() method of the class Un.

print(d.value == "Eins")          # False
print(d.value)  # Zwei
# d is an instance of Quatre
# and the value in Deux will override the value in Un.
