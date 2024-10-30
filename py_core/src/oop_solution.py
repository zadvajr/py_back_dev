""" Advanced OOP Solution"""
class Product:
    """Base class Product"""
    def __init__(self, name:str, price: float, stock: int, weight: float):
        self.name = name
        self.price = price
        self.stock = stock
        self.weight = weight

    def get_info(self):
        """get_info() method returns information about products"""
        return f"Product Name: {self.name}, Price: ${self.price}, \
        Stock: {self.stock}, Weight: {self.weight} kg"
    def apply_discount(self, discount_percentage: float):
        """applies discounted percentage"""
        discount = (discount_percentage * self.price) / 100
        return self.price - discount
    def check_stock(self, quantity):
        """check stock qty """
        if quantity <= self.stock:
            return self.stock - quantity
        return "Out of Stock"
    def calculate_shipping_cost(self):
        """calculates shipping cost"""
        shipping_cost = self.weight * 10
        return shipping_cost

class ElectronicProduct(Product):
    """Electronic product class"""
    def __init__(self, name, price, stock, weight):
        super().__init__(name, price, stock, weight)

class GroceryProduct(Product):
    """Grocery product class"""


phone = ElectronicProduct("Tecno Pova 6", 272000.0, 20, 25.0)
print(phone.calculate_shipping_cost())
