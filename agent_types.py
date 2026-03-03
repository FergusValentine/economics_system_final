from abc import ABC, abstractmethod
from agent_supply_demand import Supply, IDemand
from inventory import Inventory

class IConsumer(ABC):
    @abstractmethod
    def fulfill_demand(self, sorted_agents):
        pass

    @abstractmethod
    def get_id(self):
        pass

class IProducer(ABC):
    @abstractmethod
    def fulfill_supply(self):
        pass

    @abstractmethod
    def get_supply_name(self):
        pass

    @abstractmethod
    def get_supply_price(self):
        pass

    @abstractmethod
    def get_stock(self, product):
        pass

    @abstractmethod
    def get_id(self):
        pass

class Consumer(IConsumer):
    def __init__(self, name: str, demand: IDemand):
        self.name = name
        self.demands = demand
        self.inventory = Inventory()

    def fulfill_demand(self, sorted_agents):
        pass

    def get_id(self):
        return self.name

class Supplier(IProducer):
    def __init__(self, name: str, supply: Supply):
        self.name = name
        self.supply = supply
        self.inventory = Inventory()

    def get_stock(self, product):
        return self.inventory.get_product_stock(product)

    def get_supply_name(self):
        return self.supply.name

    def get_supply_price(self):
        return self.supply.get_price()

    def fulfill_supply(self):
        pass

    def get_id(self):
        return self.name

class Transformer(IProducer, IConsumer):
    def __init__(self, name: str, supply: Supply, demand: IDemand):
        self.name = name
        self.supply = supply
        self.demands = demand
        self.inventory = Inventory()

    def get_stock(self, product):
        pass

    def get_supply_name(self):
        return self.supply.name

    def get_supply_price(self):
        pass

    def fulfill_supply(self):
        pass

    def fulfill_demand(self, sorted_agents):
        demands = self.demands.get()

        for product in demands.values():
            product_name = product.name
            product_amount = product.amount

            demand_markets = sorted_agents[product_name]

    def get_id(self):
        return self.name