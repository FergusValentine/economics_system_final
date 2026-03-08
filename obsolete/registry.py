from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")

class IAgentRegistry(ABC, Generic[T]):
    @abstractmethod
    def get_agents(self):
        pass

    @abstractmethod
    def add_agent(self, agent: T):
        pass

    @abstractmethod
    def remove_agent(self, agent: T):
        pass

class AgentRegistry[T](IAgentRegistry[T]):
    def __init__(self):
        self.registry = []

    def get_agents(self):
        return self.registry

    def add_agent(self, agent: T):
        pass

    def remove_agent(self, agent: T):
        pass