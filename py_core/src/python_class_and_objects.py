#Python class and objects
#Python is an object oriented programming
#Almost everything in python is an object
#A class is like an object constructor or a blueprint for creating object

#creating a class - class can be created with class keyword
#create a class MyClass with a property x
class MyClass:
    x = 5

#now we can use the class MyClass to create objects as follows
p1 = MyClass()
print(p1.x)  #will print 5. because x is a property of MyClass and p1 is a object or instance of MyClass

#The __init__() function
#all classess have a function called __init__() which is always invoked whenever the class is initiated
#__init__() is used to assign values to object properties.
#NOTE: the __init__() function is called automatically every time the class is being used to create a new object.
#example:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Daniel", 33)
print(p1.name) # Will print: Daniel
print(p1.age) # Will print: 33


#The __str__() - this functions controls what should be return when the class object is represented as string
#if the __str__() function is not set, the string representation of the object is returned.
# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

# p1 = Car("Toyota", "Camry", 2024)
# print(p1) # The output will be: <__main__.Car object at 0x7feb4ea5b050>

#with __str__() 
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def __str__(self):
        return f"This car brand is: {self.brand} and it's Model is: {self.model}, {self.year} released."

p1 = Car("Toyota", "Camry", 2024)
print(p1)

#object methods