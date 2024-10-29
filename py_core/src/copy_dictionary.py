#Copy Dictionary - You cannot copy a dictionary by simply typing dict2 = dict1, because dict2 will only be a reference to dict1, and changes made in dict1 will automatically be made in dict2.
#There are ways to make a copy, one way is to use the built-in Dictionary method copy().
#Example:
#Make a copy of a dictionary using the copy() method
car = {
    "brand": "Benz",
    "model": "LS500",
    "year": 2024,
    "country": "NGN"
}
car_ref = car
car_copy = car.copy()
print("Original: ", car)
print("Copy: ", car_copy)
print("Reference: ", car_ref)

#Modify the orignal dictionary
car["year"] = 2025
print("After modification: ", car)
print("Copy after modification: ", car_copy)
print("Reference after modification: ", car_ref)

#Another way to copy a dictionary is to use the built-in method dict()
car_dict = dict(car)
print("Dictionary: ", car_dict)
#The dict() method can also be used to convert a tuple into a dictionary
#Example:
#Convert a tuple into a dictionary
car_tuple = (("brand", "Benz"), ("model", "LS500"), ("year", 2024), ("country", "NGN"))
car_dict = dict(car_tuple)
print("Tuple to Dictionary: ", car_dict)
#You can also use the dict() method to create a dictionary with specified keys and values
#Example:
#Create a dictionary with specified keys and values
car_dict = dict(brand="Benz", model="LS500", year=2024, country="NGN")
print("Specified keys and values: ", car_dict)
#Note: The keys must be strings, and the values must be valid data types.
#You can also use the dict() method to create a dictionary with specified keys and values
#Example:
#Create a dictionary with specified keys and values
car_dict = dict(brand="Benz", model="LS500", year=2024, country="NGN")
print("Specified keys and values: ", car_dict)
#Note: The keys must be strings, and the values must be valid data types.
#You can also use the dict() method to create a dictionary with specified keys and values
#Example:
#Create a dictionary with specified keys and values
car_dict = dict(brand="Benz", model="LS500", year=2024, country="NGN")
print("Specified keys and values: ", car_dict)
#Note: The keys must be strings, and the values must be valid data types.
#You can also use the dict() method to create a dictionary with specified keys and values
#Example:
#Create a dictionary with specified keys and values
car_dict = dict(brand="Benz", model="LS500", year=2024, country="NGN")
print("Specified keys and values: ", car_dict)
#Note: The keys must be strings, and the values must be valid data types.
