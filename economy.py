from agents import IAgent

from market import Market
from supply_demand_process import SupplyDemandProcess

class Economy:
    def __init__(self):
        self.market = Market()
        self.supply_demand_process = SupplyDemandProcess(self.market)

    def get_market(self):
        return self.market

    def register_agent(self, agent: IAgent):
        self.market.add_agent(agent)

    def execute_turn(self):
        self.supply_demand_process.process_demands()
        self.supply_demand_process.process_supply()
        self.market.update()

    def get_market_history(self):
        market_history = {}

        for agent in self.get_market().get_agents():
            category = agent.get_market_category()
            history = agent.get_agent_history()

            if not category in history:
                market_history[category] = {}

            if not agent in market_history[category]:
                market_history[category][agent] = {}

            for section, value in history.items():
                if not section in market_history[category][agent]:
                    market_history[category][agent][section] = value

        return market_history