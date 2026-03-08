from abc import ABC, abstractmethod

class IProduct(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_amount(self):
        pass

class IProductList(ABC):
    def get_products(self) -> dict[str, IProduct]:
        pass

    def add_product(self, product: IProduct):
        pass

    def remove_product(self, product: IProduct):
        pass

class Product(IProduct):
    def __init__(self, product_name, amount):
        self.name: str = product_name
        self.amount: int = amount

    def get_name(self) -> str:
        return self.name

    def get_amount(self) -> int:
        return self.amount

class ProductList(IProductList):
    def __init__(self):
        self.products: dict[str, IProduct] = {}

    def get_products(self) -> dict[str, IProduct]:
        return self.products

    def add_product(self, product: IProduct):
        product_name: str = product.get_name()
        self.products[product_name] = product

    def remove_product(self, product: IProduct):
        product_name: str = product.get_name()
        del self.products[product_name]