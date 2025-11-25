
data = {'name': 'Peter', 'age': 30}
person = data.copy()
print(id(data) == id(person))  # False

person = data
print(id(data) == id(person))  # True
