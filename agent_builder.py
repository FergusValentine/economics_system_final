from abc import ABC
from agent_types import Consumer, Transformer
from agent_supply_demand import IDemand, Demand, IProduct, Supply, Product


class ConsumerBuilder:
    def __init__(self, name):
        self.name = name
        self.demands: IDemand = Demand()

    def add_demands(self, *demands: IProduct):
        for demand in demands:
            self.demands.add(demand)
        return self

    def build(self):
        return Consumer(self.name, self.demands)

class TransformerBuilder:
    def __init__(self, name):
        self.name = name
        self.supply: Supply = Supply(Product("", 0))
        self.demands: IDemand = Demand()

    def add_demands(self, *demands: IProduct):
        for demand in demands:
            self.demands.add(demand)
        return self

    def add_supply(self, supply):
        self.supply.set(supply)
        return self

    def build(self):
        return Transformer(self.name, self.supply, self.demands)