#Case Insensitive Sorting - by default sort() method is case sensitive all capital letters are sorted before others
#we can use case insensitive sorting using str.lower() method to overcome that.

fruits = ["apple", "Banana", "Orange", "Kiwi", "cherry"]
print("Before: ", fruits)
fruits.sort()
print("Normal Sort: ", fruits)
fruits.sort(key=str.lower)
print("After: ", fruits)

#end
