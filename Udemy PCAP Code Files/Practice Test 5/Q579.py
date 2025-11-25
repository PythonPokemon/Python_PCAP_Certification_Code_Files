
dictionary = {}
my_list = ['a', 'b', 'c', 'd']

# for i in range(len(my_list) - 1):
for i in range(3):
    dictionary[my_list[i]] = (my_list[i], )
print(dictionary)  # {'a': ('a',), 'b': ('b',), 'c': ('c',)}

# for i in sorted(dictionary.keys()):
for i in dictionary.keys():
    k = dictionary[i]
    # print(k)  # ('a',) ('b',) ('c',)
    # print(k['0'])  # TypeError:
    # tuple indices must be integers or slices, not str
    # print(k["0"])  # TypeError: ...
    print(k[0])
    # a
    # b
    # c
