
people = {}


def add_person(index):
    if index in people:
        people[index] += 1
    else:
        people[index] = 1


add_person('Peter')
add_person('Paul')
add_person('peter')

print(len(people))  # 3
print(people)       # {'Peter': 1, 'Paul': 1, 'peter': 1}
