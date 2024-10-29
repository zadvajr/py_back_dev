"""Add set items"""
#once a set is created you cannot change its items, but you can add items using add()
fruit_set = {
    "Apple", "Banana", "Cherry", "Lemon"
}

print("Set before add: ", fruit_set)

# add
fruit_set.add("Orange")
print("Set after add: ", fruit_set) #NB: add() method takes exactly only one argument

#NOTE: the add method since sets are unordered, the index of the newly added item will be set randomly
#end