from agent_types import Transformer, Supplier, Consumer
from registry import IAgentRegistry, TransformerRegistry, SupplierRegistry, ConsumerRegistry

from economy_processes import SupplyProcess, DemandProcess

class Economy:
    def __init__(self):
        self.transformer_registry: IAgentRegistry = TransformerRegistry()
        self.supplier_registry: IAgentRegistry = SupplierRegistry()
        self.consumer_registry: IAgentRegistry = ConsumerRegistry()

        self.supply_process = SupplyProcess(self.transformer_registry, self.supplier_registry)
        self.demand_process = DemandProcess(self.transformer_registry, self.consumer_registry, self.consumer_registry)

    def register_consumer(self, agent: Consumer):
        self.consumer_registry.add_agent(agent.get_id(), agent)

    def register_supplier(self, agent: Supplier):
        self.supplier_registry.add_agent(agent.get_id(), agent)

    def register_transformer(self, agent: Transformer):
        self.transformer_registry.add_agent(agent.get_id(), agent)

    def execute_turn(self):
        self.demand_process.execute_process()
        self.supply_process.execute_process()