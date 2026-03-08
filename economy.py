from agents import IAgent

from market import Market
from supply_demand_process import SupplyProcess, DemandProcess

class Economy:
    def __init__(self):
        self.market = Market()

        self.demand_process = DemandProcess(self.market)
        self.supply_process = SupplyProcess(self.market)

    def register_agent(self, agent: IAgent):
        self.market.add_agent(agent)

    def execute_turn(self):
        self.demand_process.execute()
        self.supply_process.execute()