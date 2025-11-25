
# Yes, The map() function creates a copy of its second argument,
# and applies the first argument to it:
my_list = [1, 2, 3]
foo = list(map(lambda x: x**x, my_list))
print(foo)      # [1, 4, 27]
print(my_list)  # [1, 2, 3]

# Yes, a list comprehension becomes a generator when used
# inside round brackets (i.e., ()), not square brackets(i.e., []).
g1 = (i*i for i in range(10))
print(g1)  # <generator object <genexpr> at 0x10ec52350>
for n in g1:
    print(n, end=" ")  # 0 1 4 9 16 25 36 49 64 81
print()


# No, the yield statement must be used INSIDE functions.
def generate_numbers():
    z = 0
    while True:
        yield z * z
        z += 1


g2 = generate_numbers()
print(next(g2))  # 0
print(next(g2))  # 1
print(next(g2))  # 4


# No, The declaration of the lambda function is NOT
# the same as the declarartion of a regular function.
def f1():
    print('I am a normal function. You need the keyword def')


# This is a lambda function and you need the keyword lambda:
f2 = lambda x, y: x ** y
print(f2(2, 8))  # 256
