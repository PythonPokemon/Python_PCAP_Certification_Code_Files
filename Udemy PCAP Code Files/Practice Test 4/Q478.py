
foo = "Mary had 21 little sheep"
print(foo.split()[2].isdigit())  # True

print("Mary had 21 little sheep".split())
# ['Mary', 'had', '21', 'little', 'sheep']
print(['Mary', 'had', '21', 'little', 'sheep'][2])  # "21"
print("21".isdigit())  # True
