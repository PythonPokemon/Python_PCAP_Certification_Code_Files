
# A function that prints integers from 1 to 100:
def f1():
    for i in range(1, 101):
        print(i)


print(f1())  # None
# Not to return a value means to return "None"


# A function that returns a random integer from 1 to 100:
def f2():
    from random import randint
    return randint(1, 100)


print(f2())  # e.g. 87
# It returns the random number.


# A function that converts an uppercase letter to lowercase:
def f3(s):
    return s.lower()


print(f3('X'))  # x
# This function would return the lower letter
