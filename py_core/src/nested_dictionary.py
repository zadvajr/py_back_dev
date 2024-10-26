#Nested Dictionary - a dictionary can contain another dictionary inside of it. This is called a nested dictionary
myfamily = {
    "first": {
        "name": "Daniel Zadva Jnr",
        "age": 33,
        "city": "Lagos",
    },
    "second": {
        "name": "Panazara Daniel",
        "age": 30,
        "city": "Maiduguri"
    },
    "third": {
        "name": "Kefas Daniel Zadva",
        "age": 27,
        "city": "Chibok"
    }
}

#Access items in nested dictionary
#To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
print("The first child is : ", myfamily["first"]["name"])

#Loop through a nested dictionary as follows
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])