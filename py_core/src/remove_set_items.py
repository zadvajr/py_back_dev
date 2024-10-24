"""Remove set items using remove() and discard()"""
fruit_set = {
    "Apple", "Banana", "Cherry", "Kiwi", "Lemon", "Orange"
}

print("Original Set: ", fruit_set)

#remove "Banana" using remove()
fruit_set.remove("Banana")
print("After Remove 1: ", fruit_set)

#using discard() - remove "Cherry" with discard()
fruit_set.discard("Cherry")
print("After remove 2: ", fruit_set)

#NB: The difference between remove() and discard() is that -
# remove() will raise an error if item does not exist while discard() won't raise any error

#end
