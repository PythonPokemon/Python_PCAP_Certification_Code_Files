
try:
    # value = input("Enter a value: ")
    value = "0"
    print(int(value)/int(value))
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")  # Very bad input...
except TypeError:
    print("Very very bad input...")
except:
    print("Booo!")

print(0/0)  # ZeroDivisionError: division by zero
