"""Using asterik to unpack tuples"""
# if the number of variables is less than the number of values in the tuple,
# you can add an asterik * to the variable name and the values will be assigned
# to the variable as list

# example
fruits = ("Apple", "Banana", "Cherry", "Strawberry", "Rasberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#end
