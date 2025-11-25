
try:
    print(int("5")/0)
except ArithmeticError:
    print("arith")
except ZeroDivisionError:
    print("zero")
except:
    print("some")  # some

# print("5"/0)  # TypeError
