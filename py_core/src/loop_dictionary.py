#You can loop through a dictionary by using a for loop. when looping through a dictionary the return value are the keys of the dictionary.
#But there are other ways to return the values too.
#Loop and print all the key names in the dictionary one by one as follows
car = {
    "brand": "Benz",
    "model": "LS500",
    "year": 2024,
    "country": "NGN"
}

for key in car:
    print(key)

#To print values
for key in car:
    print(car[key])

#looping through values and printing them
for x in car.values():
    print(x)

#You can use the key() methods to return the keys in a dictionary
for x in car.keys():
    print(x)

#loop through both keys and values using items() method
for x, y in car.items():
    print(x, y)