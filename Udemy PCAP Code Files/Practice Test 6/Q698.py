
my_list = [1, 2, 3]

try:
    my_list[3] = my_list[2]
except BaseException as error:
    print(error)  # list assignment index out of range
