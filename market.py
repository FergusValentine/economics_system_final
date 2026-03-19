from agents import IAgent

class MarketCategory:
    def __init__(self, name: str):
        self.name = name
        self.average_price = 0
        self.category_list: list[IAgent] = []

    def update(self):
        self.average_price: float = self.calculate_average()

    def get_agents(self) -> list[IAgent]:
        return self.category_list

    def add_agent(self, agent: IAgent):
        self.category_list.append(agent)

    def get_average_price(self):
        return self.average_price

    def sort_by_price_ascending(self):
        self.category_list.sort(key=lambda a: a.get_market_price())

    def calculate_average(self) -> float:
        total_price = 0
        total_stock = 0

        for agent in self.category_list:
            stock = agent.get_agent_stock(self.name)

            if stock > 0:
                total_stock += stock
                total_price += agent.get_market_price() * stock

        if total_stock == 0:
            return 0

        return total_price/total_stock

class MarketRegistry:
    def __init__(self):
        self.registry: dict[str, MarketCategory] = {}

    def get_registry(self) -> dict[str, MarketCategory]:
        return self.registry

    def get_agents(self) -> list[IAgent]:
        agents: list[IAgent] = []

        for category in self.registry.values():
            for agent in category.get_agents():
                agents.append(agent)
        return agents

    def add_agent(self, agent: IAgent):
        category: str = agent.get_market_category()

        if not category in self.registry:
            self.registry[category] = MarketCategory(category)
        self.registry[category].add_agent(agent)

    def get_category(self, category: str) -> MarketCategory:
        return self.registry.get(category, None)

class Market:
    def __init__(self):
        self.market_registry: MarketRegistry = MarketRegistry()

    def update(self):
        registry = self.market_registry.get_registry()

        for category in registry.values():
            category.update()

    def get_agents(self) -> list[IAgent]:
        return self.market_registry.get_agents()

    def add_agent(self, agent: IAgent):
        self.market_registry.add_agent(agent)

    def get_category(self, category: str) -> MarketCategory:
        return self.market_registry.get_category(category)

    def create_transaction(self, buyer: IAgent, demand: str, quantity):
        market_category: MarketCategory = self.get_category(demand)
        markets = market_category.get_agents()
        demand_quantity = quantity

        for seller in markets:
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