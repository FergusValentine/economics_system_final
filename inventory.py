class Storage:
    def __init__(self):
        self.inventory = {}

    def get(self, product_name):
        return self.inventory.get(product_name, 0)

    def set(self, product_name, amount):
        self.inventory[product_name] = amount

class Inventory:
    def __init__(self):
        self.inventory = Storage()

    def get_product_stock(self, product_name):
        return self.inventory.get(product_name)

    def add_products(self, product_name, quantity):
        current = self.inventory.get(product_name)
        self.inventory.set(product_name, current + quantity)

    def remove_products(self, product_name, quantity):
        current = self.inventory.get(product_name)

        if current - quantity < 0:
            raise ValueError('Trying to remove a negative quantity')

        self.inventory.set(product_name, current - quantity)