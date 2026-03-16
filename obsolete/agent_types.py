from abc import ABC, abstractmethod
from obsolete.agent_supply_demand import Supply, IDemand
from inventory import Inventory
from market import Market
from obsolete.trade_strategy import ITradeStrategy, ProducerStrategy, ConsumptionStrategy

class IAgent(ABC):
    @abstractmethod
    def get_category(self):
        pass

class IConsumer(IAgent):
    @abstractmethod
    def fulfill_demand(self, sorted_agents):
        pass

class IProducer(IAgent):
    @abstractmethod
    def fulfill_supply(self):
        pass

    @abstractmethod
    def get_supply_name(self):
        pass

    @abstractmethod
    def get_market_price(self):
        pass

    @abstractmethod
    def get_stock(self, product):
        pass

class Consumer(IConsumer):
    def __init__(self, name: str, demand: IDemand):
        self.name = name
        self.demands = demand
        self.inventory = Inventory()
        self.trade_strategy: ITradeStrategy = ConsumptionStrategy()

    def fulfill_demand(self, sorted_agents):
        pass

    def get_category(self):
        return "Consumer"

class Supplier(IProducer):
    def __init__(self, name: str, supply: Supply):
        self.name = name
        self.supply = supply
        self.inventory = Inventory()
        self.market = Market()
        self.trade_strategy: ITradeStrategy = ProducerStrategy()

    def get_stock(self, product):
        return self.inventory.get_product_stock(product)

    def get_supply_name(self):
        return self.supply.name

    def get_market_price(self):
        return self.market.price

    def fulfill_supply(self):
        pass

    def get_category(self):
        return self.get_supply_name()

class Transformer(IProducer, IConsumer):
    def __init__(self, name: str, supply: Supply, demand: IDemand):
        self.name = name
        self.supply = supply
        self.demands = demand
        self.inventory = Inventory()
        self.market = Market()
        self.trade_strategy: ITradeStrategy = ProducerStrategy()

    def get_stock(self, product):
        return self.inventory.get_product_stock(product)

    def get_supply_name(self):
        return self.supply.name

    def get_market_price(self):
        return self.market.price

    def fulfill_supply(self):
        pass

    def fulfill_demand(self, sorted_agents):
        demanded_products = self.trade_strategy.get_demand_quantity(self, sorted_agents)
        #
        # demands = self.demands.get()
        #
        # for product in demands.values():
        #     product_name = product.name
        #     product_amount = product.amount
        #
        #     demand_markets = sorted_agents[product_name]
        #
        #     for market in demand_markets:
        #         quantity = self.trade_strategy.get_demand_quantity(self, market)

    def get_category(self):
        return self.get_supply_name()