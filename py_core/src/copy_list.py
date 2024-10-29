#copy list - you can use copy() method to copy a list

fruits = ["Apple", "Banana", "Cherry"]
copied_fruits = fruits.copy()

print("Original List Before Modification: ", fruits)
print("Copy List Before Modification: ", copied_fruits)

#modify fruits
fruits.insert(1, "Mango")

print("Original List After Modification: ", fruits)
print("Copy List After Modification: ", copied_fruits)

#end
