
class Failure(IndexError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "problem"


try:
    print("launch")          # launch
    raise Failure("ignition")
except RuntimeError as error:
    print(accident)
except IndexError as error:
    print("ignore")          # ignore
else:
    print("landing")

