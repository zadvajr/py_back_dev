#List comprehension - is a shortest way to derive a list from another list
#given a list of fruits, you want to filter elements that have letter 'a' in it and save them into a new list

fruits = ["Apple", "Banana", "Cherry", "Kiwi", "Mango", "Orange"]

newlist = [x for x in fruits if 'a' in x]

print("Original List:", fruits)
print("New List: ", newlist)

#end
