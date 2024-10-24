#Extend list - with extend() method - this enables you to add elements from another list

favorite_fruits = ["Cherry", "Orange"]
fruits = ["Apple", "Banana"]

print("Before extend(): ", favorite_fruits)
print(fruits)
fruits.extend(favorite_fruits)
print("After extend(): ", fruits)

#end
