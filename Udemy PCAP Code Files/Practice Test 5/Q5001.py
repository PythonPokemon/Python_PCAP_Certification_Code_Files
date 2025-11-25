
class Class:
    Variable = 0
    def __init__(self):
        self.value = 0

object_1 = Class()
object_1.Variable += 1
object_2 = Class()
object_2.value += 1
print(object_2.Variable + object_1.value)  # 0