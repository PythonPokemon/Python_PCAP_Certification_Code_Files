
def get_names():
    names = ['Peter', 'Paul', 'Mary', 'Jane', 'Steve']
    return names[2:]


def update_names(names):
    res = []
    for name in names:
        # res.append(name[:3].upper())
        res.append(name[0:3].upper())
    return res


print(update_names(get_names()))  # ['MAR', 'JAN', 'STE']
