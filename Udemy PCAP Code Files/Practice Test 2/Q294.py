
class Aircraft:
    def start(self):
        return "default"

    def take_off(self):
        self.start()


class FixedWing(Aircraft):
    pass


class RotorCraft(Aircraft):
    def start(self):
        return "spin"


fleet = [FixedWing(), RotorCraft()]
for airship in fleet:
    print(airship.start(), end=" ")  # default spin

print(fleet)
# [<__main__.FixedWing object at 0x1023f1850>,
# <__main__.RotorCraft object at 0x1023f2250>]
