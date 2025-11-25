
def o(p):
    def q():
        return '*' * p
    return q


r = o()  # TypeError ...
s = o()
print(r(1) + s(2))
