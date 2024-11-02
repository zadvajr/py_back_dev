#In python the boolean types represent True and False
#Any object can be tested for boolean truth value
#For example
fruits = []
print(bool(fruits)) #will print False becuase the fruits list is empty

fruits.append("Apple")
print(bool(fruits)) # will print True because it is a non empty list

#same applies for set, dict, tuple and other objects

#Objects that evaluates to False
#1. Boolean Constant False
print(bool(False)) #Outputs: False

#2. None Constant
print(bool(None)) #Outputs: False

#3. Numeric types that are zero
print(bool(0)) #Outputs: False
print(bool(0.00)) #Outputs: False
print(bool(0j)) #Outputs: False

#4. Empty sequences
print(bool([])) #Outputs: False
print(bool("")) #Outputs: False
print(bool({})) #Outputs: False

#5. Custom Objects that override the __bool() 
# method to return False
class MyClass:
    def __bool__(self):
        return False
custom_bool = MyClass()
print(bool(custom_bool)) #Outputs: False

#Boolean Operations
#1. and operation
print(False and False) # = False
print(False and True) # = False
print(True and False) # = False
print(True and True) # = True

#2. or operations
print(False or False) # = False
print(False or True) # = True
print(True or False) # = True

#3. not operations
print(not False) # = True
print(not True) # = False

#end