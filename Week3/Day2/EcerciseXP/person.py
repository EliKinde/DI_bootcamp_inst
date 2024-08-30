class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("Johan", "Doe")

#x.printname()

class Student(Person):
    pass

y = Student("Mkide", "Olsen")
y.printname()
