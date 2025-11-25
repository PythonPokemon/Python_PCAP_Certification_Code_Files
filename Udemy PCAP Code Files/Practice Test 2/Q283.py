
vect = ["alpha", "bravo", "charlie"]

print("alpha"[-1])    # a
print("bravo"[-1])    # o
print("charlie"[-1])  # e

new_vect = filter(lambda s: s[-1].upper() in ["A", "O"], vect)

print(list(new_vect))  # ['alpha', 'bravo']

for x in new_vect:
    print(x[1], end="")  # lr



