#Update Dictionary - The update() function will update the dictionary with the items with a given argument, if the item does not exist, it is added.
#the argument must be a dictionary or an iterable object with key value pairs
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)