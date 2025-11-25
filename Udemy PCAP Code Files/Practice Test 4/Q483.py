
vect = ["alpha", "bravo", "charlie"]
new_vect = map(lambda s: s[0].upper(), vect)
print(list(new_vect)[1])  # B

new_vect = map(lambda s: s[0].upper(), vect)
print(list(new_vect))     # ['A', 'B', 'C']
