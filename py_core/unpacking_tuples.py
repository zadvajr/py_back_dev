"""No module"""

#Unpacking tuples - when we create a tuple we normally assign value to it
#this is called packing a tuple.
#Packing tuple

fruits = ("Aplle", "Banana", "Cherry")

#unpacking tuples - means extracting values into respective variables
(green, yellow, red) = fruits

print(green) #Outputs - Apple
print(yellow) #Outputs - Banana
print(red) #Outputs - Cherry
#NB: The number of variables must match the number of elements in the tuple
# Otherwise you have to use * to collect the remaining items as list
#end
