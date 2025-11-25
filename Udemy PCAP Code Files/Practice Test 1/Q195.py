
class Cat:
    Species = 1

    def get_species(self):
        return 'kitty'


class Tiger(Cat):
    def get_species(self):
        return 'tiggy'

    def set_species(self):
        pass


creature = Tiger()
print(hasattr(creature, "Species"),
      hasattr(Cat, "set_species"))  # True False
