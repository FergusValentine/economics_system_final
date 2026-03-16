class Storage:
    def __init__(self):
        self.inventory: dict[str, int] = {}

    def get(self, product_name: str) -> int:
        return self.inventory.get(product_name, 0)

    def set(self, product_name: str, amount: int):
        self.inventory[product_name] = amount

class Inventory:
    def __init__(self):
        self.inventory: Storage = Storage()

    def get_product_stock(self, product_name) -> int:
        return self.inventory.get(product_name)

    def add_products(self, product_name: str, quantity: int):
        current: int = self.inventory.get(product_name)

        if current + quantity < 0:
            raise ValueError('Trying to remove a negative quantity')

        self.inventory.set(product_name, current + quantity)