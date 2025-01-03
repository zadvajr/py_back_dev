"""modules"""
from typing import Callable

def smart_divide(func: Callable[[int, int], float]):
    """decorator function"""
    def inner(a, b):
        if b == 0:
            print("OOPS! Division by Zero is Not Allowed!!")
            return None
        return func(a,b)
    return inner

@smart_divide
def divide(a, b):
    "normal function that use decorator"
    print(a / b)

divide(9, 0)
divide(9, 3)
