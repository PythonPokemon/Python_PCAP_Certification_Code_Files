
class Control:
    my_ID = 1

    def say(self):
        return self.my_ID


class Button(Control):
    my_ID = 2


class Radio(Button):
    def say(self):
        # return -self.my_ID
        return -1 * self.my_ID


element = Control()
start = Button()
selection = Radio()

print(selection.my_ID == 2)       # True
# Radio inherits from Button and therefore my_ID will be 2

print(isinstance(start, Button))  # True
# start is a direct object of Button.

print(selection is element)       # False
# The is operator check, whether two variables
# point to the same objekt in the memory.
# And selection and element are not even of the same class.

print(start.my_ID == -2)          # False
print(start.my_ID)  # 2
# start is a Button and therefore my_ID will be 2

