#Python inheritance program to update the quantity of the product in the dictionary and return the modified dictionary.

class ProductManager:
    def __init__(self):
        self.product = {}

    def add_product(self, product_name, price, quantity):
        self.product = {
            "product_name": product_name,
            "price": price,
            "quantity": quantity
        }
        return self.product

    def update_price(self, new_price):
        self.product["price"] = new_price
        return self.product

    def update_quantity(self, quantity_change):
        self.product["quantity"] += quantity_change
        return self.product


# Create an instance of the ProductManager class
manager = ProductManager()

# Add a product
product1 = manager.add_product("iPhone 12", 900.50, 10)
print("Product:", product1)

# Update the price of a product
product1 = manager.update_price(850.80)
print("\nUpdated Product:", product1)

# Update the quantity of a product
product1 = manager.update_quantity(2)
print("\nUpdated Product:", product1)
