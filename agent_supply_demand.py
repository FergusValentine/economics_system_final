class Product:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

class Supply:
    def __init__(self, product: Product):
        self.price = 0
        self.supply = 0
        self.demand = 0
        self.supply_product: Product = product

    def get_price(self):
        return self.price

    def get_product(self):
        return self.supply_product.name

    def get_product_amount(self):
        return self.supply_product.amount

class Demand:
    def __init__(self):
        self.demands: dict[str, Product]

    def get_demands(self):
        return self.get_demands()