"""Join sets"""
#There are several ways to join two or more sets in python
#1. union() and update() - joins all items from both sets 
#2. intersection() method - keeps only the duplicates
#3. difference() method - keeps items in the first set that are not present in the other sets
#4. symmetric_difference() method - keeps all the items except duplicate

# union() - returns a new set with all items from both sets
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}

set3 = set1.union(set2) #Returns - {1, 'c', 2, 3, 'b', 'a'}

print(set3)


# You can also use the pipe operator | instead of the union() method and it yields the same result
set3 = set1 | set2
print(set3)

#you can use any of the method above to join multiple sets too

#Join set and tuple
#union() method - method can be used to join a set and other iterables like list or tuple
#the result will be a set
mytuple = ("apple", "banana", "cherry")
my_set = set1.union(mytuple)
print(my_set)

#update() - inserts all items from one set to another
# it does not return new set like union, it updates the original set
set4 = {'d', 'e', 'f'}
set1.update(set4)
print(set1)

#NB: Both update and union does not return duplicates


#intersection() - returns only the duplicate
fruits = {"apple", "banana", "cherry"}
companies = {"microsoft", "apple", "google"}
common = fruits.intersection(companies) # returns - apple you can also use &
common2 = companies.intersection(fruits)
print(common)
print(common2)


#difference() - will return a new set that are contained in the first set but not in the other sets
f = {"apple", "banana", "cherry"}
c = {"microsoft", "apple", "google"}
diff_f = f.difference(c)
diff_c = c.difference(f)
print(diff_f)
print(diff_c)

#NB: you can also use - operator for difference but only applicable on sets

#symmetric_difference() - returns non duplicate items
f = {"apple", "banana", "cherry"}
c = {"microsoft", "apple", "google"}
diff = f.symmetric_difference(c)
print(diff)

#you can also use ^ for the same purpose


#end