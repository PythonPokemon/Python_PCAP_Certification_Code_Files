
def func():
    text = 'Paul'
    names = lambda x: text + ' ' + x
    return names


people = func()
print(people)  # <function func.<locals>.<lambda> at ...>
print(people('Peter'))  # Paul Peter

# For comparison:
names2 = lambda x: 'Paul' + ' ' + x
print(names2('Peter'))  # Paul Peter
