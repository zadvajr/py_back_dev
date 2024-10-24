"""Access set items"""
#set items cannot be accessed using an index or key
# you can loop through a set to access its value using for loop
# or you check if an item is in a set using the in keyword

fruits_set = {
    "Apple",
    "Banana", 
    "Cherry",
    "Lemon",
    "Orange"
}

for fruit in fruits_set:
    print(fruit)


# or check if "Lemon" is in the set
print("Banana" in fruits_set) #will return True if it exist

#end
