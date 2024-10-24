#Type hints in python - first introduced in python version 3.4+
#The reason for type hints is to annotate the variables and functions to give indication of what they are expecting
#python interpreter only checks for type at run time, you can use static type checkers to achieve type checking at compilation in python e.g. mypy

#Example: function without type
# def total_price(price_1, price_2):
#     return f"Your total bill is USD {price_1 + price_2}"

# print(total_price(30, 40)) #running that function with int arguments will work fine
#However, if you pass in a string argument you get a wrong answer as shown in the next line

# print(total_price("30", "40")) #the output will be 3040 against the correct 70

#To identify such bugs in the development we use static type checkers such as mypi,pylance,pyre, etc.

#Benefits of type hints
#with type hints it improves code suggestion and completion in ide
def total_price(price_1: int, price_2: int) -> str:
    return f"Your total bill is USD {price_1 + price_2}"

price = total_price(30, 40)
prc = total_price("30", "40")
print(price.upper())
print(prc)
