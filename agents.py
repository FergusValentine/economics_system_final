from abc import ABC, abstractmethod

from agent_history import AgentHistory
from inventory import Inventory
from market_strategy import IMarketStrategy
from product_list import IProductList, IProduct
from factory import Factory

from wallet import Wallet

import math

class IAgent(ABC):
    @abstractmethod
    def get_wallet(self) -> Wallet:
        pass

    @abstractmethod
    def add_market_demand(self, amount: int):
        pass

    @abstractmethod
    def get_market_category(self) -> str:
        pass

    @abstractmethod
    def get_agent_demand(self) -> dict[str, IProduct]:
        pass

    @abstractmethod
    def get_agent_stock(self, category) -> int:
        pass

    @abstractmethod
    def add_agent_stock(self, product_name: str, quantity: int):
        pass

    @abstractmethod
    def get_agent_history(self):
        pass

    @abstractmethod
    def fulfill_demand(self, markets):
        pass

    @abstractmethod
    def fulfill_supply(self, markets):
        pass

    @abstractmethod
    def get_market_price(self) -> float:
        pass

class Consumer(IAgent):
    def __init__(self, money: float, demand: IProductList, market_strategy: IMarketStrategy):
        self.wallet: Wallet = Wallet(money)
        self.inventory = Inventory()

        self.agent_history = AgentHistory()

        self.trade_strategy: IMarketStrategy = market_strategy
        self.input: IProductList = demand

    def get_wallet(self) -> Wallet:
        return self.wallet

    def get_agent_demand(self) -> dict[str, IProduct]:
        return self.input.get_products()

    def get_agent_stock(self, product_name: str) -> int:
        return self.inventory.get_product_stock(product_name)

    def add_agent_stock(self, product_name: str, quantity: int):
        self.inventory.add_products(product_name, quantity)

    def get_market_price(self) -> float:
        return 0

    def add_market_demand(self, amount: int):
        pass

    def get_market_category(self) -> str:
        return "Consumer"

    def get_agent_history(self):
        return self.agent_history.get_history()

    def fulfill_supply(self, markets):
        pass

    def fulfill_demand(self, markets):
        demands = self.trade_strategy.demand_function(self, markets)
        self.wallet.add_money(10)
        for demand, quantity in demands.items():
            demand_quantity = quantity

            markets.create_transaction(self, demand, demand_quantity)
        self.agent_history.record_value("money", "money", self.get_wallet().get_money())

class Producer(IAgent):
    def __init__(self, money: float, price: float, supply: IProduct, demand: IProductList, factory: Factory, market_strategy: IMarketStrategy):
        self.market_demand: int = 0
        self.market_supply: int = 0
        self.market_price: float = price

        self.agent_history = AgentHistory()

        self.wallet: Wallet = Wallet(money)
        self.inventory: Inventory = Inventory()

        self.factory: Factory = factory
        self.trade_strategy: IMarketStrategy = market_strategy

        self.input: IProductList = demand
        self.output: IProduct = supply

    def get_wallet(self) -> Wallet:
        return self.wallet

    def get_market_demand(self) -> int:
        return self.market_demand

    def add_market_demand(self, amount: int):
        self.market_demand += amount

    def reset_market_demand(self):
        self.market_demand = 0

    def get_market_supply(self) -> int:
        return self.market_supply

    def set_market_supply(self, quantity: int):
        self.market_supply = quantity

    def get_market_price(self) -> float:
        return self.market_price

    def set_market_price(self, new_price: float):
        self.market_price = new_price

    def get_market_category(self) -> str:
        return self.output.get_name()

    def get_agent_demand(self) -> dict[str, IProduct]:
        return self.input.get_products()

    def get_agent_supply(self) -> IProduct:
        return self.output

    def get_agent_stock(self, product_name: str) -> int:
        return self.inventory.get_product_stock(product_name)

    def add_agent_stock(self, product_name: str, quantity: int):
        self.inventory.add_products(product_name, quantity)

    def get_agent_history(self):
        return self.agent_history.get_history()

    def produce(self):
        product_name = self.get_market_category()
        demands = self.get_agent_demand()
        amount = []

        if len(demands) == 0:
            amount.append(self.get_market_supply())

        for demand, product in demands.items():
            recipe_amount = product.get_amount()
            stock_amount = self.get_agent_stock(demand)

            if recipe_amount == 0 or stock_amount == 0:
                return

            amount.append(math.floor(stock_amount / recipe_amount))

        supply = self.get_market_supply()
        maximum_production = min(amount)
        production = min(supply, maximum_production)

        required_production = max(supply - self.get_agent_stock(product_name), 0)
        production = min(production, required_production)

        production_value = production

        for demand, product in demands.items():
            amount = product.get_amount()
            consumed = production_value * amount

            self.add_agent_stock(demand, -consumed)

        self.add_agent_stock(product_name, production_value)

    def fulfill_supply(self, market):
        product = self.get_market_category()
        supply = self.get_market_supply()
        demand = self.get_market_demand()

        self.agent_history.record_value("Supply V Demand", "Supply", supply)
        self.agent_history.record_value("Supply V Demand", "Demand", demand)

        self.produce()
        self.agent_history.record_value("Supply V Demand", "Stock", self.get_agent_stock(self.get_market_category()))

        print(product, "Supply:", supply, "Demand:", demand, "Price:", self.get_market_price())
        if abs(supply - demand) < 0.1:
            print("converge")
        elif supply < demand:
            self.factory.add_labor(1)
        elif supply > demand:
            self.factory.remove_labor(1)

        self.factory.update_marginal_production() ### NOT NEEDED HERE

        labor = self.factory.get_labor()
        labor_cost = self.factory.get_marginal_cost(labor)
        self.agent_history.record_value("Price", "Labor_Cost", labor_cost)

        demands = self.get_agent_demand()
        demand_prices = self.trade_strategy.get_demand_prices(demands, market)
        demand_cost = sum(demand_prices.values())
        self.agent_history.record_value("Price","Demand_Cost", demand_cost)

        variable_cost = labor_cost + demand_cost
        self.set_market_price(variable_cost)
        self.agent_history.record_value("Price","Total_Cost", variable_cost)

        total_product = math.floor(self.factory.get_total_product(labor))
        self.set_market_supply(total_product)
        self.reset_market_demand()

    def fulfill_demand(self, market):
        demands = self.get_agent_demand()
        max_quantities = self.trade_strategy.demand_function(self, market)

        for demand, quantity in demands.items():
            desired_quantity = quantity.get_amount() * self.market_supply
            demand_quantity = min(desired_quantity, max_quantities[demand])

            market.create_transaction(self, demand, demand_quantity)