
class Alpha:
    def say(self):
        return "alpha"


class Beta(Alpha):
    def say(self):
        return "beta"


class Gamma(Alpha):
    def say(self):
        return "gamma"


class Delta(Beta, Gamma):
    pass


d = Delta()
b = Beta()

print(Gamma in Delta.__bases__)  # True
# Gamma is a direct superclass of Delta.

print(isinstance(d, Alpha))      # True
# d is an instance of Delta.
# Alpha is a superclass of Delta.
# Therfore d is also an instance of Alpha.

print(b is d)                    # False
# b and d are different objects
# and even of different classes.

print(d.say() == "gamma")        # False
print(d.say())  # beta
# The topic here is Method Resolution Order (MRO)
# In the inheritance list of the Delta class superclasses
# Beta is first and therefore Delta will inherit
# the say() method of the Beta class
# which will return "Beta".
