
def f(x, y):
    nom, denom = x, y
    def g():
        return nom / denom
    return g

a = f(1, 2)
b = f(3, 4)

print(a is not None)  # True
print(a != b)         # True

print(a() == 4)       # False
print(a())            # 0.5

print(b() == 4)       # False
print(b())            # 0.75
