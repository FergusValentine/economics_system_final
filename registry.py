from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from agent_types import Transformer, Supplier, Consumer
from sorter import IRegistrySorter, SupplierSorter

T = TypeVar("T")

class Registry[T]:
    def __init__(self):
        self.registry: dict[str, T] = {}

    def get(self) -> dict[str, T]:
        return self.registry

    def add(self, agent_id: str, agent: T):
        self.registry[agent_id] = agent

class IAgentRegistry(ABC, Generic[T]):
    @abstractmethod
    def get_agents(self) -> dict[str, T]:
        pass

    @abstractmethod
    def add_agent(self, agent_id, agent):
        pass

    @abstractmethod
    def get_categorized_value_ascending(self):
        pass

class ConsumerRegistry(IAgentRegistry[Consumer]):
    def __init__(self):
        self.registry: Registry[Consumer] = Registry[Consumer]()
        self.sorter = None

    def get_agents(self) -> dict[str, Consumer]:
        return self.registry.get()

    def add_agent(self, agent_id: str, agent: Consumer):
        self.registry.add(agent_id, agent)

    def get_categorized_value_ascending(self):
        pass

class SupplierRegistry(IAgentRegistry[Supplier]):
    def __init__(self):
        self.registry: Registry[Supplier] = Registry[Supplier]()
        self.sorter: IRegistrySorter = SupplierSorter()

    def get_agents(self) -> dict[str, Supplier]:
        return self.registry.get()

    def add_agent(self, agent_id: str, agent: Supplier):
        self.registry.add(agent_id, agent)

    def get_categorized_value_ascending(self):
        pass

class TransformerRegistry(IAgentRegistry[Transformer]):
    def __init__(self):
        self.registry: Registry[Transformer] = Registry[Transformer]()
        self.sorter = SupplierSorter()

    def get_agents(self) -> dict[str, Transformer]:
        return self.registry.get()

    def add_agent(self, agent_id: str, agent: Transformer):
        self.registry.add(agent_id, agent)

    def get_categorized_value_ascending(self):
        return self.sorter.sort_value_ascending(self.registry.get())