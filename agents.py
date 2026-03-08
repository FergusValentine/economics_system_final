from abc import ABC, abstractmethod

from inventory import Inventory
from trade_strategy import ITradeStrategy
from product_list import IProductList, IProduct
from factory import Factory

import math

class IAgent(ABC):
    @abstractmethod
    def fulfill_demand(self, markets):
        pass

    @abstractmethod
    def fulfill_supply(self, markets):
        pass

    @abstractmethod
    def get_agent_category(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_stock(self, category):
        pass

    @abstractmethod
    def get_agent_money(self):
        pass

class Consumer(IAgent):
    def __init__(self, money, demand, trade_strategy):
        self.money = money
        self.inventory = Inventory()

        self.trade_strategy: ITradeStrategy = trade_strategy
        self.input: IProductList = demand

    def fulfill_supply(self, markets):
        pass

    def fulfill_demand(self, markets):
        demand_quantity = self.trade_strategy.get_demand_quantity(self, markets)

    def get_agent_category(self):
        return "Consumer"

    def get_price(self):
        return 0

    def get_stock(self, category):
        return 0

    def get_agent_money(self):
        pass

class Producer(IAgent):
    def __init__(self, money, supply, demand, factory, trade_strategy):
        self.demand = 0
        self.supply = 0
        self.price = 0

        self.money = money
        self.inventory = Inventory()

        self.factory: Factory = factory
        self.trade_strategy: ITradeStrategy = trade_strategy
        self.input: IProductList = demand
        self.output: IProduct = supply

    def get_agent_demands(self):
        return self.input.get_products()

    def get_agent_supply(self):
        return self.supply

    def get_stock(self, category):
        return self.inventory.get_product_stock(category)

    def add_demand(self, amount):
        self.demand += amount

    def fulfill_supply(self, markets):
        self.factory.update_marginal_production()

        labor = self.factory.get_labor()
        price = self.factory.get_marginal_labor(labor)

        if abs(self.supply - self.demand) < 0.1:
            print("Convergence")
        elif self.supply < self.demand:
            pass
        elif self.supply > self.demand:
            pass

        self.supply = math.floor(self.factory.get_total_product(labor))
        self.demand = 0

    def fulfill_demand(self, markets):
        demand_products: dict[str, IProduct] = self.get_agent_demands()

        amount_desired = self.trade_strategy.get_demand_quantity(self)

        ## amount demanded
        desired = {}
        for demand_name, demand_product in demand_products.items():
            desired[demand_name] = demand_product.get_amount() * amount_desired
        #

        # production maximization
        # money/(d1*p1 + d2*p2 + d3*p3 + d4*p4)
        price_per_product = 0
        for demand_name, demand_product in demand_products.items():
            market_average = markets.get_market_category_average(demand_name)
            price_per_product += market_average * demand_product.get_amount()

        #
        amount_max = math.inf
        if price_per_product > 0:
            amount_max = math.floor(self.get_agent_money()/price_per_product)

        amount_purchased = min(amount_desired, amount_max)
        demanded = {}
        for demand_name, demand_product in demand_products.items():
            demanded[demand_name] = demand_product.get_amount() * amount_purchased
        #

        # indifference
        # indifference = p1/bM + p2/bM + p3/bM + p4/bM
        products = {}
        budget = 0
        for demand_name, demand_product in demand_products.items():
            market_average = markets.get_market_category_average(demand_name)
            products[demand_name] = budget/market_average


        for demand_name, demand_product in demand_products.items():
            desired = demand_product.get_amount() * demanded_units

            limited = min(desired, max_affordable)



    def get_agent_category(self):
        return self.output.get_name()

    def get_price(self):
        return self.price

    def get_agent_money(self):
        return self.money