import math
from abc import ABC, abstractmethod

class ITradeStrategy(ABC):
    @abstractmethod
    def get_demand_quantity(self, agent):
        pass

    def get_demand_cost(self, agent, market):
        pass

    @abstractmethod
    def get_shopping_list(self, agent, market):
        pass

class ConsumptionStrategy(ITradeStrategy):
    def get_demand_quantity(self, agent):
        return math.inf

    def get_shopping_list(self, agent, market):
        pass

class ProducerStrategy(ITradeStrategy):
    def get_demand_quantity(self, agent):
        return agent.get_agent_supply()

    def get_maximum_pairs(self, agent, product_prices):
        total_cost = sum(product_prices.values())

        if total_cost == 0:
            return math.inf

        return agent.get_money()/total_cost

    def get_maximized_demand(self, agent, product_prices):
        maximum_pairs = self.get_maximum_pairs(agent, product_prices)

        demands = agent.get_agent_demands()
        maximum_quantities = {}
        for product_name, product in demands.items():
            maximum_quantities[product_name] = product.get_amount() * maximum_pairs

        return maximum_quantities

    def get_demand_prices(self, agent, markets):
        demands = agent.get_agent_demands()

        market_prices = {}
        for product_name, product in demands.items():
            market_prices[product_name] = markets.get_market_category_average(product_name)
        return market_prices

    def get_shopping_list(self, agent, markets):
        prices = self.get_demand_prices(agent,  markets)

        ## indifference
        maximized_demand = self.get_maximized_demand(agent, prices)
        ##

        for product_name, product in agent.get_agent_demands().items():
            desired_quantity = product.amount * agent.get_agent_supply()

            purchase_quantity = min(desired_quantity, maximized_demand[product_name])
            pass