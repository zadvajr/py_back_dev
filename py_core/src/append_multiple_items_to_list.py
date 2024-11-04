#How to append multiple items to a list

#using a loop
# Example list
my_list = [1, 2, 3]

# Elements to append
elements_to_append = [4, 5, 6]

# Append elements using a loop
for item in elements_to_append:
    my_list.append(item)

print(my_list)  # Output: [1, 2, 3, 4, 5, 6]