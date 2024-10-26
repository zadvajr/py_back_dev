#Python functions - functions are block of code that runs only when they are called
#you can pass data known as parameter into a function and it can also return data
#there are two types of functions user-defined and built-in functions

#creating a function - in python functions are created with def keyword followed by a function name
# def hello():
#     print("Helllo from my function")

#calling a function
#to call a function use the function name followed by open and close parenthesis
# hello()


#functions arguments and parameters
#variables defined inside parenthesis during function definition is called parameters
#while values passed into a function during call is called arguments
# def welcome_user(fname): #fname is a parameter
#     print("Welcome ", fname)

# welcome_user("Daniel") #"Daniel" here is a value called argument

#Arbitrary arguments or keyword argument or variadic function - function with unknown number of arguments
def sum(*args: int):
    total = 0
    for i in args:
        total += i
    return total

print(sum(1,2,3,4,5))