
def func(n):
    try:
        print(1 / n)
    except ValueError as ve:
        print(ve)

try:
    func(0)
except ArithmeticError as ae:
    print(ae)  # division by zero
