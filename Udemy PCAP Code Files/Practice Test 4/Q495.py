
class Alpha:
    value = "Alpha"

    def say(self):
        return self.value.lower()


class Beta(Alpha):
    value = "Beta"


class Gamma(Alpha):
    def say(self):
        return self.value.upper()


class Delta(Gamma, Beta):
    pass


d = Delta()
b = Beta()

print(isinstance(d, Beta))       # True
# d is an instance of class Delta
# and therefore an instance of its superclass Beta.

print(d.say() == "BETA")         # True
print(d.say())                   # BETA
# Delta will inherit the say() method of the Gamma class
# and the value attribute of the Beta class.
# Therefore Delta's say() method will return "BETA"

print(d.value == "Alpha")        # False
print(d.value)                   # Beta
# The value attribute of the Alpha class
# will be overridden by the value attribute of the Beta class.

print(Alpha in Delta.__bases__)  # False
# The __bases__ attribute only lists the direct superclasses.
