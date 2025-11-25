
class Computer:
    def __init__(self, ram):
        self.ram = ram
        self.type = 'server'


computer = Computer(16000)
# computer = Computer()                 # TypeError: ...
# computer = Computer('client', 16000)  # TypeError: ...
# computer = Computer('server', 16000)  # TypeError: ...
