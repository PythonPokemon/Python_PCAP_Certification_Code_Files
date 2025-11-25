
class Tin:
    label = "Soup"

    def __init__(self, prefix):
        self.name = prefix + " " + Tin.label


can_1 = Tin("Tomato")
can_2 = Tin("Chicken")
print(can_1.label == can_2.label)  # True
