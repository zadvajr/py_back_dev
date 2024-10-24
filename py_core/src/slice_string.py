#Slicing a string

txt = "Hello World!"

#slice with start and end index
print("This is Original Text: ", txt)
print("Slicing from index 6 to 10: ",txt[6:10]) #prints World

#slicing by omitting the start index
print("Slicing from beginning by ommiting start index: ", txt[:5]) #prints Hello

#slicing by omitting the last index will slice to the end of the string
print("Slicing to the end: ", txt[6:])  #prints Worlds!

#slicing with negative index will start from the end of the string.
print("Slicing with negattive index: ", txt[-6:])   #prints: World!

#end
