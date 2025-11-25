
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year


x = Student('Paul', 'Wellert', 2021)
