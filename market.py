import math

from agents import IAgent

class Registry:
    def __init__(self):
        self.registry: dict[str, list[IAgent]] = {}

    def get_agents(self) -> dict[str, list[IAgent]]:
        return self.registry

    def get_agents_by_category(self, category: str) -> list[IAgent]:
        return self.registry.get(category, [])

    def add_agent(self, agent: IAgent):
        category: str = agent.get_market_category()

        if not category in self.registry:
            self.registry[category] = []

        self.registry[category].append(agent)

    def sort_registry_by_price_descending(self):
        for agents_list in self.registry.values():
            agents_list.sort(key=lambda agent: agent.get_price())

class Market:
    def __init__(self):
        self.market_registry: Registry = Registry()

    def get_agents(self) -> dict[str, list[IAgent]]:
        return self.market_registry.get_agents()

    def add_agent(self, agent: IAgent):
        self.market_registry.add_agent(agent)

    def get_category(self, demand: str) -> list[IAgent]:
        return self.market_registry.get_agents_by_category(demand)

    def create_transaction(self, buyer: IAgent, demand: str, quantity):
        demand_markets: list[IAgent] = self.get_category(demand)
        demand_quantity = quantity

        for seller in demand_markets:
            seller.add_market_demand(quantity)

            available_stock = seller.get_agent_stock(demand)
            if available_stock == 0:
                continue

            purchase_quantity = min(demand_quantity, available_stock)
            purchase_cost = purchase_quantity * seller.get_market_price()

            ##make purchase
            buyer_wallet = buyer.get_wallet()
            seller_wallet = seller.get_wallet()

            buyer_wallet.add_money(-purchase_cost)
            seller_wallet.add_money(purchase_cost)
            buyer.add_agent_stock(demand, purchase_quantity)
            seller.add_agent_stock(demand, -purchase_quantity)

            demand_quantity = demand_quantity - purchase_quantity

    def get_market_category_average(self, demand: str) -> float:
        agents_list: list[IAgent] = self.get_category(demand)

        sum_price = 0
        sum_stock = 0

        for agent in agents_list:
            stock = agent.get_agent_stock(demand)
            sum_stock += stock
            sum_price += agent.get_market_price() * stock

        if sum_stock == 0 or sum_price == 0:
            return 0

        return sum_price/sum_stock