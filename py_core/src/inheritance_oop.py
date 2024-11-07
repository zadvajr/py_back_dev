#Inheritance
class Python:
    def __init__(self):
        self.is_cool = True

class FastAPI(Python):
    pass

f = FastAPI()
print(f.is_cool)

#Output: True