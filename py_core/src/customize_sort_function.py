#Customize sort() function with keywords arguments
#You can define a function that based on which you want to sort yoru function

#For example - assuming you want to filter a list based on a particular function that checks if 'a' is in element of the list.

def custom_sort(n):
    return [x for x in n if 'a' in x]

fruits = ["banana", "cherry", "apple", "mango", "kiwi", "orange"]
print("Before Custom Sort: ", fruits)
fruits.sort(key=custom_sort)
print("After Custom Sort: ", fruits)

#end
