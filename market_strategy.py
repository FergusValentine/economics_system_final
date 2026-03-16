import math
from abc import ABC, abstractmethod

class IMarketStrategy(ABC):
    @abstractmethod
    def get_demand_prices(self, agent, market):
        pass

    @abstractmethod
    def demand_function(self, agent, market):
        pass

class ConsumerStrategy(IMarketStrategy):
    def get_demand_prices(self, demands, market):
        market_prices = {}
        for product_name, product in demands.items():
            product_average = market.get_market_category_average(product_name)
            market_prices[product_name] = product_average

        return market_prices

    def get_budget_ratio(self, demands):
        sum_amount = 0
        for demand in demands.values():
            sum_amount += demand.get_amount()

        return sum_amount / len(demands)

    def demand_function(self, agent, market):
        demands = agent.get_agent_demand()
        agent_wallet = agent.get_wallet()
        money = agent_wallet.get_money()

        prices = self.get_demand_prices(demands, market)
        budget_ratio = self.get_budget_ratio(demands)

        maximum_quantities = {}
        for product_name, price in prices.items():
            maximum_quantities[product_name] = math.floor((money * budget_ratio) / max(price, 1))

        return maximum_quantities

class ProducerStrategy(IMarketStrategy):
    def get_demand_prices(self, demands, market):
        market_prices = {}
        for product_name, product in demands.items():
            product_average = market.get_market_category_average(product_name)
            market_prices[product_name] = product_average

        return market_prices

    def demand_function(self, agent, market):
        demands = agent.get_agent_demand()
        agent_wallet = agent.get_wallet()
        money = agent_wallet.get_money()

        prices = self.get_demand_prices(demands, market)
        sum_demand_cost = sum(prices.values())
        maximum_pairs = math.floor(money / max(float(sum_demand_cost), 0.1))

        maximum_quantities = {}
        for product_name, product in demands.items():
            maximum_quantities[product_name] = product.get_amount() * maximum_pairs

        return maximum_quantities