from abc import ABC, abstractmethod
from agent_supply_demand import Supply, Demand
from inventory import Inventory

class IConsumer(ABC):
    @abstractmethod
    def fulfill_demand(self):
        pass

class IProducer(ABC):
    @abstractmethod
    def fulfill_supply(self):
        pass

class Consumer(IConsumer):
    def __init__(self, demand: Demand):
        self.demand = demand
        self.inventory = Inventory()

    def fulfill_demand(self):
        pass

class Supplier(IProducer):
    def __init__(self, supply: Supply):
        self.supply = supply
        self.inventory = Inventory()

    def fulfill_supply(self):
        pass

class Transformer(IProducer, IConsumer):
    def __init__(self, supply: Supply, demand: Demand):
        self.supply = supply
        self.demand = demand
        self.inventory = Inventory()

    def fulfill_supply(self):
        pass

    def fulfill_demand(self):
        pass