from abc import ABC, abstractmethod

from agent_types import IConsumer, IProducer
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

    def fulfill_transformer_demand(self, sorted_markets: dict[str, IConsumer]):
        transformers_dict: dict[str, IConsumer] = self.transformer_registry.get_agents()

        for agent_id, agent in transformers_dict.items():
            agent.fulfill_demand(sorted_markets)

    def fulfill_consumer_demand(self, sorted_markets: dict[str, IConsumer]):
        consumers_dict: dict[str, IConsumer] = self.consumer_registry.get_agents()

        for agent_id, agent in consumers_dict.items():
            agent.fulfill_demand(sorted_markets)

    def execute_process(self):
        sorted_markets = self.supplier_registry.get_categorized_value_ascending()
        # self.fulfill_transformer_demand(sorted_markets)

        n = self.transformer_registry.get_categorized_value_ascending()
        self.fulfill_consumer_demand(sorted_markets)

class SupplyProcess(IEconomyProcess):
    def __init__(self, transformer_registry: IAgentRegistry, supplier_registry: IAgentRegistry):
        self.transformer_registry = transformer_registry
        self.supplier_registry = supplier_registry

    def execute_process(self):
        pass