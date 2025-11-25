
data = ['Peter', 'Paul', 'Mary', 'Jane']
for d in data:
    if len(d) == 4:
        print(d)

"""
Paul
Mary
Jane
"""

print('----------')

data = ['Peter', 'Paul', 'Mary', 'Jane']
da = data[1:]
for d in data:
    print(d)

"""
Peter
Paul
Mary
Jane
"""

print('----------')

data = ['Peter', 'Paul', 'Mary', 'Jane']
for d in data:
    if len(d) != 4:
        print(d)

"""
Peter
"""

print('----------')

data = ['Peter', 'Paul', 'Mary', 'Jane']
for d in data:
    print(d)

"""
Peter
Paul
Mary
Jane
"""
