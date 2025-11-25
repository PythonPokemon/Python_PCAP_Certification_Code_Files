
class Accident(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "problem"


try:
    print("action")       # action
    raise Accident("accident")
except Accident as accident:
    print(accident)       # problem
    # print(accident.args)  # ('accident',)
else:
    print("success")
