#Join Lists - there are 3 ways to join two or more lists
#1. using concatenation operator or +
#2. using for loop and appending each element
#3. using extend() method

#joining lists with +
list1 = ['a', 'b', 'c']
list2 = [1,2,3]
list3 = list1 + list2
print("List 1: ", list1)
print("List 2: ", list2)
print("List 3: ", list3)


#joining list with for loop
fruits = ["apple", "banana", "cherry"]
favorite = ["cashew", "mango", "kiwi"]

for x in favorite:
    fruits.append(x)

print(fruits)

#using extend method
favorite.extend(list1)

print(fruits)

#end
