from abc import ABC, abstractmethod
from agent_types import IProducer, IAgent
from typing import Generic, TypeVar

class IRegistrySorter(ABC):
    @abstractmethod
    def sort_value_ascending(self, agents):
        pass

    @abstractmethod
    def sort_value_descending(self, agents):
        pass

    @abstractmethod
    def get_average_value(self, agents):
        pass

class ConsumerSorter(IRegistrySorter):
    def sort_value_ascending(self, agents):
        pass

    def sort_value_descending(self, agents):
        pass

    def get_average_value(self, agents):
        pass

class ProducerSorter(IRegistrySorter):
    def sort_value_ascending(self, supplier: dict[str, list[IProducer]]):
        sorted_agents: dict[str, list[IProducer]] = {}

        for category, values in supplier.items():
            sorted_agents[category] = sorted(values, key = lambda m: m.get_market_price())

        return sorted_agents

    def sort_value_descending(self, agents):
        pass

    def get_average_value(self, agents):
        pass