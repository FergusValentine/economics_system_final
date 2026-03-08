import math
from abc import ABC, abstractmethod

from product_list import IProduct

class ITradeStrategy(ABC):
    @abstractmethod
    def get_demand_quantity(self, agent):
        pass

class ConsumptionStrategy(ITradeStrategy):
    def get_demand_quantity(self, agent):
        return math.inf

class ProducerStrategy(ITradeStrategy):
    def get_demand_quantity(self, agent):
        return agent.get_agent_supply()
