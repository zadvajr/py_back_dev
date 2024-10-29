"""Loop through tuples with index"""
# You can also loop through tuples by referring to their index numbers
# Use range() and len() to create suitable iterable
fruits = ("Apple", "Banana", "Cherry", "Lemon", "Orange")
# for i in range(len(fruits)):
#     print(fruits[i])

for i, fruit in enumerate(fruits):
    print(i, fruits[i])
#end
