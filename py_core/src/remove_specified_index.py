# remove specified index with pop()
# pop() removes the specified index, if no arguements are provided it removes the last item in the list

fruits = ["Apple", "Banana", "Cherry", "Kiwi", "Melon", "Mango"]

print("Before pop(): ", fruits)
fruits.pop() # deletes the last item Mango
fruits.pop(1) #deletes the second item: Banana
print("After pop()", fruits)

#end
