
plane = "Blackbird"
counter = 0
# for c in plane + str(2):
for c in plane + 2:
    # TypeError: can only concatenate str (not "int") to str
    if c in ["1", "2"]:
        counter += 1
print(counter)
