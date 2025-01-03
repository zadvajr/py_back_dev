#Python conditions and if else statement
# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# These conditions can be used in several ways, most commonly in "if statements" and loops.

# An "if statement" is written by using the if keyword.

#Example
#if statement
# a = 33 
# b = 200
# if b > a:
#     print("b is greater than a")

# Elif
# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
a = 200
b = 200
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")