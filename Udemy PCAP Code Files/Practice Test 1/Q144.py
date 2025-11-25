
import random
people = ['Peter', 'Paul', 'Mary', 'Jane']
random.shuffle(people)
print(people)  # e.g. ['Mary', 'Jane', 'Peter', 'Paul']

# people.shuffle()            # AttributeError: ...
# random.shuffleList(people)  # AttributeError: ...

# shuffle(people) only works with the following import:
from random import shuffle
shuffle(people)
print(people)  # e.g. ['Paul', 'Peter', 'Jane', 'Mary']
