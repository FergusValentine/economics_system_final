from abc import ABC, abstractmethod

class IProduct(ABC):
    @abstractmethod
    def get_name(self):
        pass
    @abstractmethod
    def get_amount(self):
        pass

class Product(IProduct):
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def get_name(self):
        return self.name

    def get_amount(self):
        return self.amount

class IDemand(ABC):
    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def remove(self, item):
        pass

class ISupply(ABC):
    @abstractmethod
    def set(self, product: Product):
        pass

class Demand(IDemand):
    def __init__(self):
        self.demands: dict[str, Product] = {}

    def get(self):
        return self.demands

    def add(self, item: Product):
        self.demands[item.name] = item

    def remove(self, item):
        if item.name in self.demands:
            del self.demands[item.name]

    def replace(self, item:Product, replacement:Product):
        self.remove(item)
        self.add(replacement)

class Supply(ISupply):
    def __init__(self, product):
        self.product: IProduct = product

    def set(self, product: IProduct):
        self.product = product

    @property
    def name(self):
        return self.product.get_name()

    @property
    def amount(self):
        return self.product.get_amount()