#Remove Dictionary Items - there are several methods to remove dictionary items.

#1. pop() - the pop method removes items with the specified key name
car = {
    "brand": "Benz",
    "model": "LS500",
    "year": 2024,
    "country": "NGN"
}
print("Before pop(): ", car)

#To remove the country key and its value using pop() do as follow
deleted_value = car.pop("country", "Key Not found") #the second argument is a default value if the key is not found
print("After pop(): ", car)
print("Deleted value: ",deleted_value)

#NOTE: the pop() method returns the deleted value, if the key is not found return default if given, else raise KeyError


#2. popitem() - removes the last inserted item. In python version before 3.7 random items were removed
person = {
    "name": "daniel",
    "height": 1.75,
    "color": "black",
    "age": 33
}
print("Before: ", person)

#Assuming you want to delete the last inserted item "age" you use the popitem() method as follow
deleted_item = person.popitem()
print("After: ", person)
print("Deleted: ", deleted_item)



#3. del - removes item with the specified key name
student = {
    "name": "Daniel",
    "course": "Python Backend",
    "age": 33,
    "graduation": 2025
}
print("Before: ", student)

#To delete student age do as follows
del student["age"]
print("After: ", student)

#the del keyword can delete the dictionary entirely as follows
#Assuming we want to delete the student dictionary,
del student
# print(student) # assessing the dictionary after del will issue name error

#4. The clear() method empties the dictionary
#assuming we want to empty our car dictionary. We do as follows
car.clear()
print(car) # returns an empty dictionary
