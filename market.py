import math

from agents import IAgent

class Registry:
    def __init__(self):
        self.registry: dict[str, list[IAgent]] = {}

    def get_agents(self):
        return self.registry

    def get_agents_by_category(self, category):
        return self.registry.get(category, [])

    def add_agent(self, agent):
        category = agent.get_agent_category()

        if not category in self.registry:
            self.registry[category] = []
        self.registry[category].append(agent)

    def sort_registry_by_price_descending(self):
        for agents_list in self.registry.values():
            agents_list.sort(key=lambda agent: agent.get_price())

class Market:
    def __init__(self):
        self.market_registry: Registry = Registry()

    def get_agents(self):
        return self.market_registry.get_agents()

    def add_agent(self, agent: IAgent):
        self.market_registry.add_agent(agent)

    def get_market_category(self, category):
        return self.market_registry.get_agents_by_category(category)

    def get_market_category_average(self, category):
        agents_list = self.market_registry.get_agents_by_category(category)

        sum_price = 0
        sum_stock = 0

        for agent in agents_list:
            sum_price += agent.get_price()
            sum_stock += agent.get_stock(category)

        if sum_stock == 0:
            return 0
        elif sum_price == 0:
            return math.inf

        return sum_stock / sum_price