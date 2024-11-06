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
#To create a class that inherits the functionality from another class, send the parent class as a 
# parameter when creating the child class
class Student(Person):
    pass

p1 = Student("Mary", "Michael")
p1.printname()

#adding an init function to child class
class Student(Person):
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
#NOTE: when you add the __init__() function to the child class, the child class will no longer 
# inherit __init__() function from parent class.
#The child's init function will override the inheritance of the parent's init function
# p1 = Student("Daniel", "Zadva")
# p1.printname()


#To keep the inheritance of the parent's init function, you need to add a call to it.
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
#this block will keep the inheritance of the Student class

#Using the super() function
#Python has a function super() that will make the child class inherit all the properties and methods from the paretn's class
class Student(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)

