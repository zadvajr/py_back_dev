#Sorting lists in descending order
#sort() method accepts an arguments reverse which if set to True will reverse the sorting operations on the list

#for example
#on apha list
fruits = ["apple", "mango", "orange", "kiwi", "cherry", "banana"]
print("Fruits Lists Before Sorting: ", fruits)
fruits.sort(reverse=True) #reverses the sorting operations
print("Fruits Lists After Sorting: ", fruits)

#sorting number list in descending
users_age = [50, 23, 18, 45, 17, 28 48]
print("Users Age Before Sorting: ", users_age)
users_age.sort(reverse=True)
print("Users Age After Sorting: ", users_age)

#end
