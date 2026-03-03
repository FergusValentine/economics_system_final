from abc import ABC, abstractmethod

from agent_types import IConsumer
from registry import IAgentRegistry

class IEconomyProcess(ABC):
    @abstractmethod
    def execute_process(self):
        pass

class DemandProcess(IEconomyProcess):
    def __init__(self, transformer_registry: IAgentRegistry, supplier_registry: IAgentRegistry, consumer_registry: IAgentRegistry):
        self.transformer_registry = transformer_registry
        self.supplier_registry = supplier_registry
        self.consumer_registry = consumer_registry

    def fulfill_transformer_demand(self, sorted_markets):
        for agent_id, agent in self.transformer_registry.get_agents():
            agent.fulfill_demand()

    def fulfill_consumer_demand(self, sorted_markets):
        consumers_dict: dict[str, IConsumer] = self.consumer_registry.get_agents()

        for agent_id, agent in consumers_dict.items():
            agent.fulfill_demand()

    def execute_process(self):
        sorted_markets = None #supplier #transformers

        self.fulfill_transformer_demand(sorted_markets)
        self.fulfill_consumer_demand(sorted_markets)

class SupplyProcess(IEconomyProcess):
    def __init__(self, transformer_registry: IAgentRegistry, supplier_registry: IAgentRegistry):
        self.transformer_registry = transformer_registry
        self.supplier_registry = supplier_registry

    def execute_process(self):
        pass