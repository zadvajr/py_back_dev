#Range of index - you can specify range of indexes by specifying where to start and where to end
# when specifying the range the return value is a new list with some set of values

fruits = ["Apple", "Banana", "Cherry", "Orange", "Melon", "Kiwi", "Mango"]

#return third, fourth, and fifth element
print(fruits[2:5]) #the last index is not inclusive - Cherry, Orange, Melon

#omitting the start index - it will start from the beginning
print(fruits[:5]) #prints Apple, Banana, Cherry, Orange, Melon

#omitting the end index - it will access items up to the end of the list
print(fruits[2:]) #prints - Orange, Melon, Kiwi, Mango

#negative index range e.g. -5:3
print(fruits[-5:-3]) # prints - Cherry, Orange

#end
