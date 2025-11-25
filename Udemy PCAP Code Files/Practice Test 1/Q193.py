
class Economy:
    def __init__(self):
        self.econ_attr = True


class Business(Economy):
    def __init__(self):
        super().__init__()
        self.busn_attr = False


econ_a = Economy()
econ_b = Economy()
busn_a = Business()
busn_b = busn_a
print(isinstance(busn_a, Economy)
      and isinstance(econ_a, Business), end=" ")  # False
print(busn_b is busn_a or econ_a is econ_b)       # True

print()
print(isinstance(busn_a, Economy))   # True
print(isinstance(econ_a, Business))  # False

print()
print(busn_b is busn_a)  # True
print(econ_a is econ_b)  # False

