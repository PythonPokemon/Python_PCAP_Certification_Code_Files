
try:
    # first_prompt = input("Enter the first value: ")
    first_prompt = "kangaroo"
    a = len(first_prompt)
    print(a)                          # 8
    # second_prompt = input("Enter the second value: ")
    second_prompt = "0"
    b = len(second_prompt) * 2
    print(b * 2)                      # 2
    print(8 / 2)                      # 4.0
    print(a / b)                      # 4.0
except ZeroDivisionError:
    print("Do not divide by zero!")
except ValueError:
    print("Wrong value.")
except:
    print("Error.Error.Error.")
