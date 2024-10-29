#Access Dictionary Items
#You can access dictionary items by referring to its keys in square brackets or using the get() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
y = thisdict.get("year")
print(x)
print(y)

# get keys 
z = thisdict.keys()
print(z)
