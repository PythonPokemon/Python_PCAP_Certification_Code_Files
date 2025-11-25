
box = {}
jars = {}
crates = {}

box['biscuit'] = 1
box['cake'] = 3

jars['jam'] = 4

crates['box'] = box
crates['jars'] = jars

print(len(crates[box]))  # TypeError: unhashable type: 'dict'
print(len(crates['box']))  # 2
print(crates['box'])       # {'biscuit': 1, 'cake': 3}
print(crates)
# {'box': {'biscuit': 1, 'cake': 3}, 'jars': {'jam': 4}}
