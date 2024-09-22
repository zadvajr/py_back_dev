#Updating tuples - tuples are unchangeable, meaning you cannot add, remove or update tuple values once created.
#However, there are some workarounds, you can convert the tuple into list, make your changes and then convert it back to tuple as follows

fruits = ("apple", "banana", "cherry", "kiwi", "lemon")

#fruits[1] = "orange" #this line will cause an error

print("Before: ",fruits)
#convert to list and try the changes again
fruits_list = list(fruits)
fruits_list[1] = "orange"
fruits = tuple(fruits_list)
print("After: ", fruits)

#end
