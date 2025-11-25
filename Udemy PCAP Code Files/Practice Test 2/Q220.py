
def increment(c, num):
    c.count += 1
    num += 1


class Counter:
    def __init__(self):
        self.count = 0


counter = Counter()
number = 0

for i in range(0, 100):
    increment(counter, number)

print(
    "counter is "
    + str(counter.count)
    + ", number of times is "
    + str(number)
)
# counter is 100, number of times is 0
