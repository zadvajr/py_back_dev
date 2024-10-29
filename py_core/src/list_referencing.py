#List referencing - you can't copy a list by simply assigning it to another list as follow, that will give you only a list reference
#meaning that any changes made to any of the list will affect the other.

#for example

list1 = ["apple", "banana", "cherry", "kiwi", "lemon", "mango", "orange"]
print("List 1: ", list1)

list2 = list1 #referencing the list
print("List 2: ", list2)

#now I will make changes to list1
list1.append("cashew")
print("List 1 After Modification: ", list1)
print("List 2 After Modification: ", list2)


#end
