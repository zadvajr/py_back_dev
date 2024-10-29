#Python Inheritance - This allow us to define a class that inherits all the methods and properties from another class
#Parent class - is the class being inherited from, also called base class
#Child class - is the  class that inherits from another class, also called derived class

#create a parent class called Person
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)

p1 = Person("Daniel", "Zadva Jnr")
p1.printname()

#Create a child class
#To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class
class Student(Person):
    pass

p1 = Student("Mary", "Michael")
p1.printname()

