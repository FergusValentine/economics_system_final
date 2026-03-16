from agents import Consumer, Producer
from factory import Workplace
from product_list import IProductList, IProduct, ProductList, Product
from factory import Factory, Appliance

class CreateConsumer:
    def __init__(self):
        self.money = 0
        self.input: IProductList = ProductList()
        self.market_strategy = None

    def set_money(self, money):
        self.money = money
        return self

    def add_demand(self, demand: IProduct):
        self.input.add_product(demand)
        return self

    def set_market_strategy(self, trade_strategy):
        self.market_strategy = trade_strategy
        return self

    def build(self) -> Consumer:
        agent = Consumer(self.money, self.input, self.market_strategy)
        return agent

class CreateProducer:
    def __init__(self):
        self.money = 0
        self.price = 0
        self.factory = None
        self.output: IProduct = Product("", 0)
        self.input: IProductList = ProductList()
        self.market_strategy = None

    def set_money(self, money):
        self.money = money
        return self

    def set_price(self, price):
        self.price = price
        return self

    def add_demand(self, demand: IProduct):
        self.input.add_product(demand)
        return self

    def set_supply(self, supply: IProduct):
        self.output = supply
        return self

    def set_factory(self, factory: Factory):
        self.factory = factory
        return self

    def set_market_strategy(self, market_strategy):
        self.market_strategy = market_strategy
        return self

    def build(self) -> Producer:
        agent = Producer(self.money, self.price, self.output, self.input, self.factory, self.market_strategy)
        return agent

class CreateFactory:
    def __init__(self):
        self.labor = 0
        self.efficiency = 0
        self.wages = 0

        self.workplace = Workplace()

    def set_labor(self, labor):
        self.labor = labor
        return self

    def set_efficiency(self, efficiency):
        self.efficiency = efficiency
        return self

    def set_wages(self, wages):
        self.wages = wages
        return self

    def add_appliance(self, appliance: Appliance):
        self.workplace.add_appliance(appliance)
        return self

    def build(self):
        factory = Factory(self.labor, self.wages, self.efficiency, self.workplace)
        return factory

class CreateAppliance:
    def __init__(self, optimal_labor, max_production):
        self.optimal_labor = optimal_labor
        self.max_production = max_production

    def build(self):
        appliance = Appliance(self.optimal_labor, self.max_production)
        return appliance