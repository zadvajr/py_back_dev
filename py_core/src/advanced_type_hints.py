"""Advanced type hints"""
from typing import List, Tuple, Dict, Union, Optional


# Adavanced type hints Before python 3.9 you cannot annotate ...
# #advanced data structures such as list, tuples, and dictionary directly.
# but from version 3.9 python introduced a module called typing.

#for python version 3.9 and lower versions

price: List[int] = [200, 300, 400, 500]
immutable_price: Tuple[int, int, int] = (30, 40, 50)
price_dict: Dict[str, int] = {
    "item1": 200,
    "item2": 400
}


#from python 3.10 upward you can use the list, tuple, and dict keywords directly.
price: list[int] = [200, 900, 100]
immutable_price: tuple[int, int, int] = (200, 400, 300)
price_dict: dict[str, int] = {
    "item1": 200,
    "item2": 500
}

print(price)
print(type(price))
print(immutable_price)
print(type(immutable_price))
print(price_dict)
print(type(price_dict))


#annote complex data types as follows
x: List[Union[int, float]] = [2.3, 4, 5, 4.5]
print(x)
print(type(x))


#Annote return type of a function
def inr_usd(value: float) -> Optional[float]: #Union[float, None] replaced with optional
    """inr_usd() - returns float or None"""
    try:
        conversion_factor = 75
        value = value / conversion_factor
        return value
    except TypeError:
        return None
print(inr_usd("400"))
print(inr_usd(400))

#Custom type
Image = List[List[int]]
image = [[1, 2, 3], [4, 5, 6]]

def flatten_image(src: Image) -> List:
    """Custom type"""
    flatten_list = []
    for sublist in src:
        for item in sublist:
            flatten_list.append(item)
    return flatten_list

print(flatten_image(image))

#Type annotate custom classes
