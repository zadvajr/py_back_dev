# Advanced Question: Object-Oriented Programming in Python

You are tasked with developing a more advanced system to manage products for an e-commerce platform using Object-Oriented Programming (OOP) in Python. You will create a base class Product and two specific product types: ElectronicProduct and GroceryProduct. Additionally, you will implement more complex functionality such as stock management, bulk discounts, and calculating delivery charges based on product type.

## Requirements:

1. Base Class: Product
   - Attributes:
     - name: A string representing the name of the product.
     - price: A float representing the price of the product.
     - stock: An integer representing the number of items available in stock.
     - weight: A float representing the weight of the product in kilograms.
   - Methods:
     - get_info(): Returns a string in the format: "Product Name: <name>, Price: $<price>, Stock: <stock>, Weight: <weight> kg".
     - apply_discount(discount_percentage): Reduces the product price by the given percentage.
     - check_stock(quantity): Checks if the requested quantity is available. If available, reduce the stock by that quantity; otherwise, return an "Out of stock" message.
     - calculate_shipping_cost(): Returns the shipping cost based on the product’s weight. For simplicity, assume $10 per kilogram.

2. Derived Class: ElectronicProduct (Inherits from Product)
   - Additional Attributes:
     - warranty_years: An integer representing the warranty period in years.
     - brand: A string representing the brand of the electronic product.
   - Overridden Method:
     - get_info(): Returns the product information in the format: "Electronic Product: <name> (Brand: <brand>), Price: $<price>, Warranty: <warranty_years> years, Stock: <stock>, Weight: <weight> kg".
   - Additional Method:
     - calculate_warranty_extension(extra_years): Extends the warranty by the given number of years and returns the new warranty period.

3. Derived Class: GroceryProduct (Inherits from Product)
   - Additional Attributes:
     - expiration_date: A string representing the expiration date of the product.
     - is_perishable: A boolean indicating whether the item is perishable.
   - Overridden Method:
     - get_info(): Returns the product information in the format: "Grocery Product: <name>, Price: $<price>, Expiration Date: <expiration_date>, Stock: <stock>, Weight: <weight> kg, Perishable: <is_perishable>".
   - Additional Method:
     - check_if_expired(current_date): Compares the current date with the expiration date and returns whether the product is expired.

4. Tasks:
   - Create an instance of ElectronicProduct named "Laptop" (Brand: "Dell"), priced at $1500, with a 3-year warranty, weighing 2.5 kg, and 10 items in stock.
   - Create an instance of GroceryProduct named "Milk", priced at $4, with an expiration date of "2024-11-15", weighing 1 kg, 50 items in stock, and marked as perishable.
   
   - For each product:
     - Print the detailed product information using get_info().
     - Apply a 15% discount to the laptop and print the updated information.
     - Check if you can order 5 units of each product, and reduce the stock accordingly.
     - Calculate the shipping cost for each product.
     - For the laptop, extend the warranty by 2 more years.
     - For the milk, check if it is expired given today's date (assume today's date is "2024-10-01").

## Example of Expected Output:

Electronic Product: Laptop (Brand: Dell), Price: $1500.00, Warranty: 3 years, Stock: 10, Weight: 2.5 kg
Grocery Product: Milk, Price: $4.00, Expiration Date: 2024-11-15, Stock: 50, Weight: 1.0 kg, Perishable: True

After 15% discount:
Electronic Product: Laptop (Brand: Dell), Price: $1275.00, Warranty: 3 years, Stock: 10, Weight: 2.5 kg

Order 5 units of Laptop: Successful, Stock Left: 5
Order 5 units of Milk: Successful, Stock Left: 45

Shipping cost for Laptop: $25.00
Shipping cost for Milk: $10.00

Extended warranty for Laptop: 5 years
Is Milk expired? False





Your code should print the following
Electronic Product: Laptop (Brand: Dell), Price: $1500.00, Warranty: 3 years, Stock: 10, Weight: 2.5 kg
Grocery Product: Milk, Price: $4.00, Expiration Date: 2024-11-15, Stock: 50, Weight: 1.0 kg, Perishable: True

After 15% discount:
Electronic Product: Laptop (Brand: Dell), Price: $1275.00, Warranty: 3 years, Stock: 10, Weight: 2.5 kg

Order 5 units of Laptop: Successful, Stock Left: 5
Order 5 units of Milk: Successful, Stock Left: 45

Shipping cost for Laptop: $25.00
Shipping cost for Milk: $10.00

Extended warranty for Laptop: 5 years
Is Milk expired? False