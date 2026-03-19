from market import Market

class SupplyDemandProcess:
    def __init__(self, market: Market):
        self.market: Market = market

    def process_demands(self):
        agent_list = self.market.get_agents()

        for agent in agent_list:
            agent.fulfill_demand(self.market)

    def process_supply(self):
        agent_list = self.market.get_agents()

        for agent in agent_list:
            agent.fulfill_supply(self.market)