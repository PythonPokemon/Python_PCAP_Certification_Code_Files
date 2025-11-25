
class Dog:

    def __init__(self, breed):
        self.breed = breed

    def bark(self):
        print('Wuff')


dog = Dog('German Shepherd')
print(dog.breed)  # German Shepherd
dog.bark()        # Wuff
