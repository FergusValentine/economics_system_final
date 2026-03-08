from market import Market

class DemandProcess:
    def __init__(self, market: Market):
        self.market: Market = market

    def execute(self):
        agent_lists = self.market.get_agents()

        for agent_list in agent_lists.values():
            for agent in agent_list:
                agent.fulfill_demand(self.market)

class SupplyProcess:
    def __init__(self, market: Market):
        self.market: Market = market



    def execute(self):
        agent_lists = self.market.get_agents()

        for agent_list in agent_lists.values():
            for agent in agent_list:
                agent.fulfill_supply(self.market)