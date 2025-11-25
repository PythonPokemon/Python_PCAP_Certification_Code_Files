
def my_fun():
    # for num in [0, 1, 2]:
    for num in range(3):
        yield num


for i in my_fun():
    print(i)
"""
0
1
2
"""
